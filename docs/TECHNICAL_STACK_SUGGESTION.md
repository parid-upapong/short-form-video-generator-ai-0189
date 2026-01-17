# Recommended Tech Stack for Implementation

- **Frontend**: Next.js 14 (App Router) + Tailwind CSS + Framer Motion (for smooth UI).
- **Video Player/Canvas**: Remotion.dev (for programmatic video rendering) or Video.js.
- **Backend**: Python (FastAPI) - specifically for heavy lifting with AI libraries.
- **AI Models**:
    - **Transcription**: OpenAI Whisper (v3).
    - **Logic/Highlights**: GPT-4o or Claude 3.5 Sonnet (Analyzing transcripts for "hooks").
    - **Vision**: MediaPipe or YOLOv8 (for face tracking and reframing logic).
- **Video Processing**: FFmpeg (via Fluent-ffmpeg) + AWS Lambda or Modal.com for GPU scaling.
- **Database**: PostgreSQL (Supabase) for project metadata + Vector DB (Pinecone) for semantic search within videos.