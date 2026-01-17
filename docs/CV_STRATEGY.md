# Computer Vision Strategy: Smart Auto-Framing

## 1. The Problem
Long-form content is usually 16:9 (Landscape). TikTok/Reels require 9:16 (Portrait). Simply cropping the center often loses the speaker when they move or if they aren't centered.

## 2. Our Solution: Active Subject Tracking
We utilize a multi-stage CV pipeline:
1.  **Detection Layer:** Using MediaPipe BlazeFace for ultra-fast facial landmark detection.
2.  **Tracking Logic:** Instead of hard-cuts, we use a **Weighted Moving Average (WMA)** to calculate the crop window's X-axis. This mimics a professional camera operator following the subject smoothly.
3.  **Heuristic Overrides:** If no face is detected (e.g., an over-the-shoulder shot), the engine defaults to the last known position or the center of the frame to maintain continuity.

## 3. Future Enhancements
- **Multi-Speaker Switching:** Implement "Speaker Diarization" combined with CV to cut between two people in a podcast format automatically.
- **Action Saliency:** Use Saliency Maps to track moving objects (e.g., a ball in sports or a product in a review) even if no face is present.
- **Automated Zooms:** Dynamically change the crop height (zoom in) during high-energy moments identified by the audio analysis engine.