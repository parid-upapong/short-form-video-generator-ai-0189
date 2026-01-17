from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User, Referral

router = APIRouter(prefix="/api/v1/growth", tags=["growth"])

@router.post("/referral/claim")
async def claim_referral_reward(referral_code: str, current_user_id: str, db: Session = Depends(get_db)):
    """
    Logic for the Growth Loop:
    When a new user signs up with a code, both the referrer and referee 
    get 30 free AI credits.
    """
    referrer = db.query(User).filter(User.referral_code == referral_code).first()
    if not referrer:
        raise HTTPException(status_code=404, detail="Invalid referral code")

    # Prevent self-referral
    if referrer.id == current_user_id:
        raise HTTPException(status_code=400, detail="Cannot refer yourself")

    # Logic to add credits
    REWARD_CREDITS = 30
    referrer.ai_minutes_balance += REWARD_CREDITS
    
    # Track the conversion
    new_referral = Referral(
        referrer_id=referrer.id,
        referee_id=current_user_id,
        status="completed"
    )
    
    db.add(new_referral)
    db.commit()
    
    return {"message": f"Success! {REWARD_CREDITS} minutes added to your account."}