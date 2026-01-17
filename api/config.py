import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "VIRAL-FLOW API"
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/viralflow")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME", "viral-flow-storage")
    FFMPEG_BINARY: str = os.getenv("FFMPEG_BINARY", "ffmpeg")
    
    # Callback URL for worker to notify API of completion
    WORKER_CALLBACK_URL: str = os.getenv("WORKER_CALLBACK_URL", "http://api:8000/internal/callback")

settings = Settings()