# Video Processing Pipeline Stages

To achieve "Minutes instead of Hours," the pipeline follows a parallel-execution strategy where possible.

| Stage | Process | Technology | Output |
| :--- | :--- | :--- | :--- |
| **0. Ingestion** | URL Download / Chunked Upload | yt-dlp / S3 Multipart | Raw MP4 |
| **1. Extraction** | Audio Stripping & Low-Res Proxy | FFmpeg | .wav & .mp4 (360p) |
| **2. Transcription**| Speech-to-Text with Timestamps | OpenAI Whisper (Large-v3) | JSON Transcript |
| **3. Detection** | Face/Object Tracking | MediaPipe / YOLOv8 | Motion Coordinates |
| **4. Analysis** | Viral Score & Segment Extraction | GPT-4o / Claude 3.5 | Start/End Timestamps |
| **5. Composition** | Smart Cropping & Caption Burn-in | FFmpeg + MoviePy | Final 9:16 Clip |
| **6. Packaging** | Thumbnail Gen & Metadata Prep | ImageMagick | .zip / .mp4 bundle |

## Optimization: The "Pre-computation" Trick
We generate the "Viral Candidates" list using only the transcript and low-res proxy. High-res rendering only happens once the user confirms a selection, or starts in the background for the top-3 scoring clips to provide "Instant Preview."