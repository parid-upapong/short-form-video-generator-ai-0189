# Infrastructure Scaling & Cost Management

## 1. GPU Orchestration
As the user base grows, we will move from fixed GPU workers to **Karpenter (EKS)** managed nodes:
- Scale to 0 at night (UTC).
- Use **NVIDIA Triton Inference Server** for serving Whisper and YOLO models to maximize throughput per GPU.

## 2. Storage Tiering
- **Hot Tier (S3 Standard):** Videos processed in the last 7 days.
- **Warm Tier (S3 Infrequent Access):** Project assets for 30 days.
- **Cold Tier (Glacier):** Archival after 30 days of inactivity.

## 3. Bottleneck Mitigation
- **Cold Starts:** Keep a "Warm Pool" of GPU workers during peak creator hours (14:00 - 22:00 EST).
- **FFmpeg Concurrency:** Limit FFmpeg threads per worker to prevent OOM (Out of Memory) crashes on 4K source files.
- **Prefetching:** Start transcription extraction as soon as the first 5MB of a video is downloaded.