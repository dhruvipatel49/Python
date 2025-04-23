import os
import shutil

new_directory = 'new_subdirectory'
os.makedirs(new_directory, exist_ok=True)

source_file = 'source_subdirectory/example.txt'
shutil.copy(source_file, new_directory)