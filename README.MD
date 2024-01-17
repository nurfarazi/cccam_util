# IMOU Camera Video Collection Utility

This utility, `vid.py`, is designed for owners of IMOU cameras who want an easy way to collect videos from the memory card.

## Prerequisites

Ensure you have Python installed on your machine. This script was tested with Python 3.12.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing `vid.py`.
3. Run the script with the following command:

```bash
python vid.py
```

By default, the script will search for video files in the /Users/nurfarazi/Downloads/cctv footage directory and copy them to the /Users/nurfarazi/Downloads/cctv footage/output directory.

Customizing Source and Destination Folders
You can customize the source and destination folders by modifying the source_folder and destination_folder variables in vid.py.

source_folder = '/path/to/your/source/folder'
destination_folder = '/path/to/your/destination/folder'

Replace /path/to/your/source/folder and /path/to/your/destination/folder with your actual source and destination paths.


To customize the source and destination folders in the vid.py script, you need to modify the source_folder and destination_folder variables in the script.

Here's how you can do it:

Open the vid.py script in your text editor or IDE.
Locate the following lines:

```
source_folder = '/path/to/your/source/folder'
destination_folder = '/path/to/your/destination/folder'
```

Replace '/path/to/your/source/folder' with the path to the directory you want to copy files from.
Replace '/path/to/your/destination/folder' with the path to the directory you want to copy files to.
Save the changes and run the script.
Remember to use absolute paths and ensure that the paths are correctly formatted for your operating system. For example, on Windows, you would use backslashes (\) instead of forward slashes (/).





