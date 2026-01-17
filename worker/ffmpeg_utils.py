import ffmpeg
import logging

logger = logging.getLogger(__name__)

def generate_ffmpeg_cmd(input_path, output_path, start, end, focal_x):
    """
    Constructs an FFmpeg filter chain to:
    1. Trim the video
    2. Smart crop to 9:16 (TikTok style) based on focal_x
    3. Scale to 1080x1920
    """
    duration = end - start
    
    # Probe input for dimensions
    probe = ffmpeg.probe(input_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    # Calculate 9:16 crop dimensions
    # Target: height stays same, width becomes (height * 9/16)
    target_w = int(height * (9 / 16))
    
    # Calculate crop 'x' offset based on focal point
    # We try to center the crop around focal_x, but clamp to edges
    center_x = int(width * focal_x)
    offset_x = center_x - (target_w // 2)
    offset_x = max(0, min(offset_x, width - target_w))

    stream = (
        ffmpeg
        .input(input_path, ss=start, t=duration)
        .filter('crop', target_w, height, offset_x, 0)
        .filter('scale', 1080, 1920)
        .output(output_path, 
                vcodec='libx264', 
                pix_fmt='yuv420p', 
                crf=23, 
                preset='fast',
                acodec='aac')
        .overwrite_output()
    )
    
    return stream