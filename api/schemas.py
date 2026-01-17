from pydantic import BaseModel, Field
from typing import List, Optional

class ClipRequest(BaseModel):
    video_id: str
    source_url: str
    start_time: float = Field(..., description="Start offset in seconds")
    end_time: float = Field(..., description="End offset in seconds")
    target_aspect_ratio: str = "9:16"
    focal_point_x: float = 0.5  # Normalized 0-1, from SubjectDetector
    focal_point_y: float = 0.5
    output_format: str = "mp4"

class ClipResponse(BaseModel):
    job_id: str
    status: str
    message: str

class JobStatus(BaseModel):
    job_id: str
    status: str
    progress: int
    output_url: Optional[str] = None