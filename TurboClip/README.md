# ⚡▶ TurboClip: Rev up your video editing speed
A Python script to speed up video files using MoviePy
From the article [Article](https://gustavo-espindola.medium.com/)

![Preview](https://github.com/gustavoespindola/learnwithai/blob/main/TurboClip/demo_c.gif?raw=true)

## Features
**Easy to Use** TurboClip is a simple, easy-to-use script that requires minimal setup and configuration, making it accessible to users of all skill levels.
**Automatic Video Processing** TurboClip can automatically process the latest video file in a specified input directory.
**Video Speed Adjustment** Users can adjust the speed of the video by specifying a speed factor, allowing for faster or slower playback.
**Customizable Output** The output file name can be customized using the current date and time, ensuring unique file names for each processed video.
**Error Handling** The script includes error handling to catch and print any exceptions that occur during the video processing, ensuring that the script doesn't crash unexpectedly.
**Input and Output Directory Management** TurboClip can manage input and output directories, making it easy to organize and process video files.
**Fast Video Rendering** TurboClip uses the moviepy library to render videos quickly and efficiently, making it suitable for large-scale video processing tasks.
**Flexibility** The script allows users to adjust the speed factor and input/output directories to suit their specific needs.

## Usage
- Create an Input directory and add the video file you want to speed up.
- Run the script using Python (e.g., python turboclip.py).
- The script will automatically process the latest video file in the Input directory and save the sped-up video to the Output directory.

## Configuration:
- Adjust the speed_factor variable in the main() function to change the speed of the output video.
- Modify the input_dir and output_dir variables to change the input and output directories.

## Requirements
- Python 3.10
- MoviePy library (install using pip install moviepy)

## Note
- Make sure to create the Input and Output directories in the same directory as the script.
- The script will overwrite any existing file with the same name in the Output directory.

## License
This project is licensed under the MIT License.

## Author
- This application was created by [Gustavo Espíndola](https://github.com/gustavoespindola). If you have any questions, feedback or requests, please contact me.
