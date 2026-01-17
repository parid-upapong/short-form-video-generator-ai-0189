import pytest
from playwright.sync_api import Page, expect

def test_viralize_workflow_e2e(page: Page):
    """
    Tests the full UI flow: Login -> Dashboard -> Viralize.
    Ensures the UI correctly reflects the 'AI Synthesis' state.
    """
    # 1. Login
    page.goto("https://app.viralflow.ai/auth")
    page.fill('input[name="email"]', "test-creator@example.com")
    page.fill('input[name="password"]', "password123")
    page.click('button[type="submit"]')
    
    # 2. Upload/Select Video
    page.goto("https://app.viralflow.ai/dashboard")
    page.click('text=New Viral Project')
    
    # Simulate pasting a YouTube URL
    page.fill('input[placeholder*="YouTube"]', "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    page.click('button:has-text("Viralize Now")')
    
    # 3. Verify AI Processing State
    # Check for the dynamic progress bar defined in USER_FLOW_CORE.md
    expect(page.locator("text=AI is finding viral gold...")).to_be_visible()
    
    # 4. Wait for Highlight Studio
    # Increased timeout to account for GPU processing
    page.wait_for_url("**/highlights", timeout=60000)
    
    # 5. Verify Highlights Grid
    clips = page.locator(".highlight-card")
    expect(clips).to_have_count(3) # Expect at least 3 viral candidates
    
    # Check for Viral Score badge
    first_score = clips.nth(0).locator(".viral-score")
    expect(first_score).to_contain_text("%")