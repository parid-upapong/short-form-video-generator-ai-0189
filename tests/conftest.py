import pytest
import time
import requests
from api.config import settings

@pytest.fixture
def api_client():
    """Returns the base URL for the API under test."""
    return "http://localhost:8000"

@pytest.fixture
def sample_video_url():
    """A standard 1080p 60s video for consistent benchmarking."""
    return "https://viral-flow-public.s3.amazonaws.com/test-assets/benchmark_v1.mp4"

@pytest.fixture
def wait_for_render():
    """Helper to poll for clip completion."""
    def _wait(clip_id, timeout=120):
        start_time = time.time()
        while time.time() - start_time < timeout:
            resp = requests.get(f"{settings.WORKER_CALLBACK_URL}/status/{clip_id}")
            if resp.json()["status"] == "COMPLETED":
                return resp.json()
            time.sleep(2)
        raise TimeoutError(f"Clip {clip_id} failed to render within {timeout}s")
    return _wait