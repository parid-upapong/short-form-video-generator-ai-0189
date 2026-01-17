import cv2
import os
from .core.detector import SubjectDetector
from .core.cropper import SmartCropper

class ViralVideoProcessor:
    """
    The main engine that consumes a landscape video and outputs a 
    subject-tracked portrait video for TikTok/Reels.
    """
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.detector = SubjectDetector()
        self.cropper = SmartCropper()

    def process_video(self):
        cap = cv2.VideoCapture(self.input_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Define output properties (9:16)
        target_h = height
        target_w = int(height * (9/16))
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_path, fourcc, fps, (target_w, target_h))

        print(f"Starting Smart Crop: {width}x{height} -> {target_w}x{target_h}")

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # 1. Detect Subject
            # Optimization: Run detection every N frames for performance, 
            # but here we run every frame for maximum tracking precision.
            center_x, _ = self.detector.get_subject_center(frame)
            
            # 2. Calculate Crop
            x_min, x_max, _ = self.cropper.get_crop_coordinates(center_x, width, height)
            
            # 3. Perform Crop
            cropped_frame = frame[0:height, x_min:x_max]
            
            # 4. Resize (if necessary, though logic above matches height)
            final_frame = cv2.resize(cropped_frame, (target_w, target_h))
            
            out.write(final_frame)
            
            frame_count += 1
            if frame_count % 100 == 0:
                print(f"Processed {frame_count} frames...")

        cap.release()
        out.release()
        self.detector.close()
        print(f"Processing complete: {self.output_path}")

if __name__ == "__main__":
    # Example usage for testing
    processor = ViralVideoProcessor("raw_podcast.mp4", "viral_clip_9_16.mp4")
    processor.process_video()