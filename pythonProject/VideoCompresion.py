import imageio_ffmpeg as iio_ffmpeg
import cv2
import numpy as np
import subprocess
from skimage.metrics import structural_similarity as ssim

def compress_video(input_path, output_path, bitrate='800k'):
    ffmpeg_path = iio_ffmpeg.get_ffmpeg_exe()
    command = [ffmpeg_path, '-i', input_path, '-b:v', bitrate, '-preset', 'slow', output_path, '-y']
    subprocess.run(command, check=True)

def get_video_info(video_path):
    ffmpeg_path = iio_ffmpeg.get_ffmpeg_exe()
    command = [ffmpeg_path, '-i', video_path]
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)
    output = result.stderr
    
    width, height, bitrate = "Unknown", "Unknown", "Unknown"
    for line in output.split('\n'):
        if "Stream #0:" in line and "Video:" in line:
            parts = line.split(",")
            for part in parts:
                if "x" in part and "[" not in part:
                    width, height = part.strip().split("x")[:2]
                if "kb/s" in part:
                    bitrate = part.strip()
            break
    return {'bitrate': bitrate, 'width': width, 'height': height}

def calculate_ssim(frame1, frame2):
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(frame1_gray, frame2_gray, full=True)
    return score

def compare_video_quality(original_path, compressed_path):
    cap_orig = cv2.VideoCapture(original_path)
    cap_comp = cv2.VideoCapture(compressed_path)
    
    if not cap_orig.isOpened() or not cap_comp.isOpened():
        return None
    
    ssim_scores = []
    while True:
        ret1, frame1 = cap_orig.read()
        ret2, frame2 = cap_comp.read()
        if not ret1 or not ret2:
            break
        ssim_scores.append(calculate_ssim(frame1, frame2))
    
    cap_orig.release()
    cap_comp.release()
    return np.mean(ssim_scores) if ssim_scores else None

if __name__ == '__main__':
    input_video = r'C:\Users\Chetan\Downloads\miocreate_faceswap.mp4'
    output_video = r'C:\Users\Chetan\OneDrive\Documents\GitHub\Practice\pythonProject\compressed.mp4'

    compress_video(input_video, output_video, bitrate='800k')
    
    original_info = get_video_info(input_video)
    compressed_info = get_video_info(output_video)
    print("Original:", original_info)
    print("Compressed:", compressed_info)
    
    avg_ssim = compare_video_quality(input_video, output_video)
    print("SSIM:", avg_ssim)
