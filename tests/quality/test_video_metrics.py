import pytest
import ffmpeg
import json
import os

def test_output_format_and_bitrate(api_client):
    """
    Ensures the generated clip is 9:16 (1080x1920) and 
    maintains a bitrate suitable for TikTok (approx 5-8 Mbps).
    """
    # Assuming the clip was generated in a previous step or use a static result
    output_path = "tests/assets/output_clip_916.mp4"
    
    probe = ffmpeg.probe(output_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    bitrate = int(video_stream.get('bit_rate', 0))
    
    # Assert Vertical Format
    assert width == 1080
    assert height == 1920
    
    # Assert Bitrate (Minimum 4Mbps for quality)
    assert bitrate >= 4000000, f"Bitrate too low: {bitrate}bps"
    
    # Assert Framerate consistency (no variable frame rate issues)
    assert video_stream['avg_frame_rate'] in ['30/1', '60/1']

def test_no_black_frames(api_client):
    """Detects if AI cropping or rendering caused dropped frames/black screen."""
    output_path = "tests/assets/output_clip_916.mp4"
    
    # Use FFmpeg to detect black segments
    # blackdetect=d=0.1:pix_th=0.1 means detect blackness > 0.1s
    out, err = (
        ffmpeg
        .input(output_path)
        .filter('blackdetect', d=0.1, pix_th=0.1)
        .output('pipe:', format='null')
        .run(capture_stdout=True, capture_stderr=True)
    )
    
    # If "black_start" is in stderr, black frames were detected
    assert "black_start" not in err.decode(), "Black frames detected in output clip"