import pytest
import time
import requests

def test_render_factor_benchmarking(api_client, sample_video_url, wait_for_render):
    """
    Validates that the render speed meets the 'Minutes not Hours' requirement.
    Target: Render Factor < 0.5
    """
    payload = {
        "video_url": sample_video_url,
        "clip_definitions": [
            {"start_time": 10, "end_time": 40} # 30 second clip
        ]
    }
    
    start_wall_clock = time.time()
    
    # Trigger Render
    response = requests.post(f"{api_client}/v1/clips/generate", json=payload)
    assert response.status_code == 202
    clip_id = response.json()["job_id"]
    
    # Wait for completion
    result = wait_for_render(clip_id)
    end_wall_clock = time.time()
    
    processing_time = end_wall_clock - start_wall_clock
    video_duration = 30 
    render_factor = processing_time / video_duration
    
    print(f"\nRender Factor: {render_factor:.2f} (Time: {processing_time:.2f}s for {video_duration}s video)")
    
    # Fail if rendering takes longer than 50% of the video duration
    assert render_factor < 0.5, f"Rendering too slow: RF {render_factor}"