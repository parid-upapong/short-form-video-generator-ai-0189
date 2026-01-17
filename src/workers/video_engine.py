import ffmpeg
from celery import Celery

app = Celery('viral_flow', broker='redis://localhost:6379/0')

@app.task(queue='cpu_tasks')
def process_smart_crop(input_path, output_path, focus_x, focus_y):
    """
    Crops a 16:9 video to 9:16 centered around the focus coordinates
    (face tracking data provided by GPU worker).
    """
    probe = ffmpeg.probe(input_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    # Calculate 9:16 crop width based on height
    target_width = int(height * (9/16))
    
    # Ensure crop doesn't go out of bounds
    x_offset = max(0, min(focus_x - (target_width / 2), width - target_width))

    (
        ffmpeg
        .input(input_path)
        .crop(x_offset, 0, target_width, height)
        .output(output_path, vcodec='libx264', crf=18, preset='fast')
        .overwrite_output()
        .run()
    )
    return {"status": "success", "path": output_path}

@app.task(queue='gpu_tasks')
def generate_transcription(audio_path):
    """
    Uses Whisper to generate high-accuracy transcription with word-level timestamps.
    """
    # Logic for loading model and processing
    # model = whisper.load_model("large")
    # result = model.transcribe(audio_path)
    pass