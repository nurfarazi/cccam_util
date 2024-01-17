import os
import shutil
import subprocess
import glob 

def collect_video_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mkv', '.mov', '.flv', '.dav')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.copy2(source_path, destination_path)

# Example usage
source_folder = '/Users/nurfarazi/Downloads/cctvfootage'
destination_folder = '/Users/nurfarazi/Downloads/outputOfCCTV'

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)


# join all the files and make a single video file
def join_video_files(source_folder, destination_folder, output_filename):
    # Create a temporary file
    with open('temp.txt', 'w') as f:
        for path in glob.glob(f'{source_folder}/*.dav'):
            f.write(f"file '{path}'\n")

    # Use the temporary file as input for ffmpeg
    command = f'ffmpeg -f concat -safe 0 -i temp.txt -c copy -ignore_unknown {destination_folder}/{output_filename}'
    subprocess.call(command, shell=True)

    # Remove the temporary file
    os.remove('temp.txt')
    
    
collect_video_files(source_folder, destination_folder)
    
join_video_files(destination_folder, destination_folder, 'final.mp4')
    
