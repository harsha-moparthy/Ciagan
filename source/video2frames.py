import cv2
import os
import argparse

def video_to_frames(video_path, output_dir, fps,width=None, height=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(video_fps / fps)
    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            if width and height:
                frame = cv2.resize(frame, (width, height))
            frame_filename = os.path.join(output_dir, f"{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Saved {saved_count} frames to {output_dir}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert video to frames")
    parser.add_argument("--input", type=str, help="Path to the input video file")
    parser.add_argument("--output", type=str, help="Directory to save the output frames")
    parser.add_argument("--fps", type=int, help="Frames per second to extract",default=1)
    parser.add_argument("--width", type=int, help="Width of the output frame")
    parser.add_argument("--height", type=int, help="Height of the output frame")

    args = parser.parse_args()
    video_to_frames(args.input, args.output, args.fps,args.width, args.height)