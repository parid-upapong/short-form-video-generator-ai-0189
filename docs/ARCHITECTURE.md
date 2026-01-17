# System Architecture: Viral-Flow Scalable Pipeline

## 1. High-Level Overview
The architecture is designed as an **Event-Driven Microservices** system to handle intensive computational loads associated with video processing and AI inference.

## 2. Component Stack
- **API Gateway:** FastAPI (Python) for high-performance async I/O.
- **Task Queue:** Redis + Celery for distributed task management.
- **Blob Storage:** AWS S3 or Cloudflare R2 (for egress cost optimization).
- **Database:** PostgreSQL (Metadata/User data) + Pinecone (Vector DB for semantic search within videos).
- **Compute:** 
    - **CPU Workers:** FFmpeg operations, file handling.
    - **GPU Workers:** Whisper (Transcription), Auto-Framing (Computer Vision), LLM Analysis.

## 3. Data Flow Diagram
1. **Ingest:** User uploads or submits a URL -> API saves metadata -> Uploads to S3.
2. **Trigger:** API emits a `VIDEO_UPLOADED` event to Redis.
3. **Transcription:** GPU Worker picks up task -> Runs Whisper -> Saves JSON transcript to S3.
4. **Intelligence:** LLM Worker analyzes transcript + visual cues -> Identifies timestamps for viral clips.
5. **Synthesis:** FFmpeg Worker crops 16:9 to 9:16 using face-tracking coordinates -> Overlays captions -> Renders final clip.
6. **Delivery:** Notify user via WebSockets/Push.

## 4. Scalability Strategy
- **Horizontal Scaling:** Workers scale independently based on queue depth.
- **Spot Instances:** Utilize AWS Spot or Lambda GPU for cost-effective rendering.
- **CDN:** Global delivery of rendered clips via CloudFront.