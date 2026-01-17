from celery import Celery
import os
import requests
from .ffmpeg_utils import generate_ffmpeg_cmd
from api.config import settings

celery_app = Celery('tasks', broker=settings.REDIS_URL)

@celery_app.task(bind=True)
def process_video_clip_task(self, job_id, source_url, start_time, end_time, focal_x, focal_y):
    """
    Background worker task to download, transcode, and upload the clip.
    """
    input_file = f"/tmp/input_{job_id}.mp4"
    output_file = f"/tmp/output_{job_id}.mp4"
    
    try:
        # 1. Download source (Simulated)
        # In production: requests.get(source_url) or boto3 download
        self.update_state(state='PROGRESS', meta={'progress': 10})
        
        # 2. Transcode with FFmpeg
        cmd = generate_ffmpeg_cmd(source_url, output_file, start_time, end_time, focal_x)
        cmd.run(capture_stdout=True, capture_stderr=True)
        
        self.update_state(state='PROGRESS', meta={'progress': 80})
        
        # 3. Upload to S3 (Simulated)
        # s3_client.upload_file(output_file, settings.S3_BUCKET_NAME, f"clips/{job_id}.mp4")
        final_url = f"https://storage.googleapis.com/{settings.S3_BUCKET_NAME}/clips/{job_id}.mp4"
        
        # 4. Notify API of completion
        # In real life, we'd update the DB here
        return {"status": "completed", "output_url": final_url}

    except Exception as e:
        self.update_state(state='FAILURE', meta={'error': str(e)})
        raise e
    finally:
        # Cleanup temp files
        if os.path.exists(input_file): os.remove(input_file)
        if os.path.exists(output_file): os.remove(output_file)