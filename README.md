# File Organizer

### A simple Python script that organizes files in a folder based on their file extensions

## Features 
- Checks Weather the given folder exists in the computer and contains files.
- Automatically detects file types by their extension.
- Moves files in to categorized folders of the same type
- Supports common file types (images, documents, audio, videos, code, etc)
- You can edit the extensions mapping in the extensions.py file as you liked it to be.

## Requirements
- Python 3
- No external libraries
 - os
 - shutil
 - glob
 - time (optional)


## How to use
1. Download the script
2. Run the script
   - in windows `python fileOrganizer.py`
   - in Mac `python3 fileOrganizer.py`
3. Enter the folder path (to be organized) when prompted
4. Files will be sorted into sub folders based on their type. that's it.


## Customization
### Since we're going to organize files by extension, 
### it totally makes sense to put the files of the same type (such as mp3, wav)
### on the same folder (such as "audio"), below Python dictionary maps each extension to a type, 
### feel free to edit on your needs to the extensions.py file:
