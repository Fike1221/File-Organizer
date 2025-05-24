from helpers import *


def manage_folders():
    """Accepts full path name of the folder and organizes files in that folder"""
    path = input("Enter the folder name (absolute path), whose files to be sorted: ")

    # check weather the path exists
    if check_path(path):
        sort_files(path)


def init():
    """Initialize the program"""
    keep_sorting = True
    while keep_sorting:
        manage_folders()
        keep_sorting = input("Do you went to continue 'yes/no' (default is no)? ").lower() in 'yes'



# check weather this file is not imported from any other files
if __name__ == '__main__':
    init()
    # sleep_two()
