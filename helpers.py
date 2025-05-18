import os
import shutil
import glob
import time

from pathlib import Path
from extensions import extensions


def execution_time(function):
    """Decorator function that measures the execution time for functions"""
    def wrapper():
        start_time = time.time()

        function()

        end_time = time.time()
        print(f"Executed in {end_time - start_time} seconds")

    return wrapper


@execution_time
def sort_files(path: str | Path) -> None:
    """Accepts a directory path (absolute) and groups the files in that folder creating sub folders"""
    total_files = 0
    wanna_know_detail = 0
    for extension, folder_name in extensions.items():
        # get all files in the given folder
        files = glob.glob(os.path.join(path, f'*.{extension}'))

        if wanna_know_detail:
            print(f"{len(files)} {folder_name} Files found with extension {extension}") if files else None

        # Check weather the folder exists and the files array is not empty
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            if wanna_know_detail:
                print(f"Creating {folder_name} folder...")
            # Create the folder if it doesn't exist
            os.mkdir(os.path.join(path, folder_name))

        # construct new path name for the newly added folder
        dst_folder = os.path.join(path, folder_name)

        # move the files to the destination (new) folder
        move_files(files, dst_folder)

        total_files += len(files)
    print(f"{total_files} Files organized successfully...")


def move_files(files: list[str], dst_folder: str | bytes) -> None:
    """Accepts a list of file names (absolute path) and destination folder name (absolute path) and moves all the
    specified files to the determined folder"""
    for file in files:
        # move individual files to the corresponding folder
        file_name = os.path.basename(file)
        destination = os.path.join(dst_folder, file_name)

        shutil.move(src=file, dst=destination)


def check_path(path: str | Path) -> bool:
    """Accepts absolute path as parameter and checks if the path exists and if it is a folder and if it contains
    files"""

    # creating a path instance
    path = Path(path)

    # check if the path exists
    if not Path.exists(path) or not path.is_dir():
        print("❌ The folder does not exist. Make sure You have inserted the right path (absolute) to your folder .")
        return False

    # check if the path includes files
    elif not any(p.is_file() for p in path.iterdir()):
        print("❌ Your folder is empty. Make sure you have inserted the right path (absolute) to your folder.")
        return False
    else:
        return True



