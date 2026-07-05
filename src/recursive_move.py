import os
import shutil

def get_files(filepath):
    
    files = []
    # files = os.listdir(filepath)
    for item in os.listdir(filepath):
        full_path = os.path.join(filepath, item)
        if os.path.isfile(full_path):
            files.append(full_path)
        else:
            files.extend(get_files(full_path))
      
    return files

def copy_files(source, destination):
    if os.path.exists(source):
        if os.path.exists(destination):
            shutil.rmtree(destination)
        os.makedirs(destination)
        files = get_files(source)
        for items in files:
            print("Copying {items} to {destination}")
            shutil.copy(items,destination)
