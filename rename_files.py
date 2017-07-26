import os

def rename_files():

    path = r"/Users/codex/Documents/prank"

    file_list = os.listdir(path)

    saved_path = os.chdir(path)

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
