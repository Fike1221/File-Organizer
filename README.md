# **File Organizer**

### A simple Python script that organizes files in a folder based on their file extensions

## **Features** 

- The program receives the absolute path of the folder name that contains the files to be organized
- The program Checks Whether the given folder exists in the computer and whether it contains files.
- Automatically detects file types by their extension.
- Moves files in to categorized folders of the same type
- Supports common file types (images, documents, audio, videos, code, etc)
- You can edit the extensions mapping in the extensions.py file as you liked it to be.

## **Requirements**

- Python 3
- No external libraries needed just use
  - os
  - shutil
  - glob
  - Path from pathlib
  - time (optional)


## **How to use**

1. Download the the program
2. Open terminal and Navigate to this programs directory by `cd 'your directory name (absolute path)'`
3. Run the program 
   - in windows `python fileOrganizer.py`
   - in Mac or Linux `python3 fileOrganizer.py`
4. Enter the folder path (that contains files to be organized) when prompted
5. Files will be sorted into sub folders based on their type. that's it.


## **Customization**

### Since we're going to organize files by extension, it totally makes sense to put the files of the same type (such as mp3, wav)on the same folder (such as "audio"), in the extensions.py file there is python dictionary that maps each extension to a their file type, feel free to edit this extensions.py file based on your needs.
