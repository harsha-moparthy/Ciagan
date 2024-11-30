import cv2
import os
import numpy as np
from scipy.interpolate import interp1d

def create_video_with_spline_interpolation(input_folder, output_video, fps=30):
    # Get all image file names sorted by frame order
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
    if not image_files:
        raise ValueError("No image files found in the input folder.")
    
    # Read the first image to get dimensions
    first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width, layers = first_image.shape
    
    # Create a video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    
    # Load all frames
    frames = [cv2.imread(os.path.join(input_folder, img)) for img in image_files]
    
    # Generate interpolated frames
    for i in range(len(frames) - 1):
        video.write(frames[i])  # Write the original frame
        # Perform spline interpolation between current and next frame
        for alpha in np.linspace(0, 1, fps // 2, endpoint=False):  # Adjust fps//2 for smoother transitions
            interpolated_frame = cv2.addWeighted(frames[i], 1 - alpha, frames[i + 1], alpha, 0)
            video.write(interpolated_frame)
    
    # Write the last frame
    video.write(frames[-1])
    
    # Release the video writer
    video.release()
    print(f"Video saved as {output_video}")

# Parameters
input_folder = '../results/'  # Folder containing the image frames
output_video = 'output_video.mp4'  # Output video file name
fps = 1  # Frames per second for the output video

# Create the video
create_video_with_spline_interpolation(input_folder, output_video, fps)
