import mediapipe as mp
import cv2
import numpy as np

class SubjectDetector:
    """
    Detects the primary subject (face/upper body) in a frame 
    to provide coordinates for smart cropping.
    """
    def __init__(self, confidence_threshold=0.5):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=1, # 1 for far-range (full body/half body), 0 for short-range
            min_detection_confidence=confidence_threshold
        )

    def get_subject_center(self, frame):
        """
        Returns the (x, y) normalized coordinates of the primary subject's center.
        If no subject is found, returns (0.5, 0.5).
        """
        results = self.face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        if not results.detections:
            return 0.5, 0.5 # Default to center

        # For simplicity, track the first/most confident face
        primary_subject = results.detections[0]
        bbox = primary_subject.location_data.relative_bounding_box
        
        # Calculate center of the bounding box
        center_x = bbox.xmin + (bbox.width / 2)
        center_y = bbox.ymin + (bbox.height / 2)
        
        return center_x, center_y

    def close(self):
        self.face_detection.close()