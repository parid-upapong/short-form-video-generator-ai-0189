from fastapi import FastAPI, HTTPException, BackgroundTasks
from .schemas import ClipRequest, ClipResponse, JobStatus
from .worker import process_video_clip_task
from .config import settings
import uuid

app = FastAPI(title=settings.PROJECT_NAME)

# In-memory store for demo; replace with Redis/Postgres in production
jobs = {}

@app.post("/clips/generate", response_model=ClipResponse)
async def generate_clip(request: ClipRequest):
    """
    Endpoint to trigger the transcoding and clipping process.
    This pushes the task to the Celery worker queue.
    """
    job_id = str(uuid.uuid4())
    
    # Initialize job state
    jobs[job_id] = {"status": "pending", "progress": 0}
    
    # Trigger Celery Task
    # Note: process_video_clip_task.delay() would be used with actual Celery
    process_video_clip_task.delay(
        job_id=job_id,
        source_url=request.source_url,
        start_time=request.start_time,
        end_time=request.end_time,
        focal_x=request.focal_point_x,
        focal_y=request.focal_point_y
    )
    
    return {
        "job_id": job_id,
        "status": "queued",
        "message": "Clip generation initiated"
    }

@app.get("/clips/status/{job_id}", response_model=JobStatus)
async def get_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return {
        "job_id": job_id,
        **jobs[job_id]
    }