import os
from moviepy.editor import VideoFileClip, vfx
from datetime import datetime

def get_latest_file(path):
    try:
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        return max(paths, key=os.path.getctime)
    except Exception as e:
        print(f"An error occurred while getting the latest file: {str(e)}")

def process_video(input_path, output_path, speed_factor):
    try:
        # Load video
        clip = VideoFileClip(input_path)

        # Speed up video
        clip = clip.fx(vfx.speedx, speed_factor)

        # Export video
        clip.write_videofile(output_path, codec='libx264')
    except Exception as e:
        print(f"An error occurred while processing the video: {str(e)}")
# 19mil - usd
def main():
    try:
        # Define input and output directories
        input_dir = './Input'
        output_dir = './Output'

        # Get the most recent video
        latest_file = get_latest_file(input_dir)

        # Define speed factor
        speed_factor = 1.5  # Adjust this value as needed

        # Define output file name
        output_file = f'{output_dir}/{datetime.now().strftime("%Y%m%d%H%M%S")}.mp4'

        # Process video
        process_video(latest_file, output_file, speed_factor)
    except Exception as e:
        print(f"An error occurred in main: {str(e)}")

if __name__ == "__main__":
    main()
