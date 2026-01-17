import numpy as np

class SmartCropper:
    """
    Calculates the 9:16 crop window based on subject coordinates 
    and applies smoothing to prevent jittery camera movement.
    """
    def __init__(self, target_ratio=(9, 16), smoothing_window=15):
        self.target_ratio = target_ratio
        self.smoothing_history = []
        self.smoothing_window = smoothing_window

    def _smooth_coordinate(self, new_val):
        self.smoothing_history.append(new_val)
        if len(self.smoothing_history) > self.smoothing_window:
            self.smoothing_history.pop(0)
        return sum(self.smoothing_history) / len(self.smoothing_history)

    def get_crop_coordinates(self, center_x, frame_width, frame_height):
        """
        Calculates x_min and x_max for a 9:16 crop centered on center_x.
        """
        # Smooth the center_x to make the 'camera' movement professional
        smoothed_x = self._smooth_coordinate(center_x)
        
        target_w = int(frame_height * (self.target_ratio[0] / self.target_ratio[1]))
        
        # Calculate pixel-based center
        pixel_center_x = int(smoothed_x * frame_width)
        
        x_min = pixel_center_x - (target_w // 2)
        x_max = x_min + target_w
        
        # Boundary constraints: Ensure the crop box doesn't go out of frame
        if x_min < 0:
            x_min = 0
            x_max = target_w
        elif x_max > frame_width:
            x_max = frame_width
            x_min = frame_width - target_w
            
        return x_min, x_max, target_w