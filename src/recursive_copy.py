import os, shutil

# recursively get file list, copy file if file, if folder create folder and repeat from start
def recursive_folder_copy(source_path, dest_path):
    files = os.listdir(source_path)
    for file in files:
        source_content_path = os.path.join(source_path, file)
        dest_content_path = os.path.join(dest_path, file)
        if os.path.isfile(source_content_path):
            print(f"Copying file: '{source_content_path}' to '{dest_path}'.")
            shutil.copy(source_content_path, dest_content_path)
        else:
            os.mkdir(dest_content_path)
            recursive_folder_copy(source_content_path, dest_content_path)

# remove and recreate empty destination path if it exists otherwise create one
def folder_clean(path):
    print(f"Cleaning '{path}'.")
    shutil.rmtree(path) # remove folder and subdirs
    print(f"Verifying destination folder removal...")
    if not os.path.exists(path): # verify folder does not exist
        print("Destination folder removal successful.\nCreating new empty folder.")
        os.mkdir(path) # create the folder
        print("Folder created.")
    else:
        raise Exception("Folder was not deleted.\nCanceling operation.")

# verify folder presences, raise errors, debug and run functions.
def recursive_copy(source_path, dest_path):
    print("Initiating folder cleaner...")
    if os.path.exists(dest_path):
        folder_clean(dest_path) # folder cleaner function
    else:
        print(f"Directory '{dest_path}' does not exist.\nCreating empty directory '{dest_path}'...")
        os.mkdir(dest_path)
    print("Cleaning complete.\n")
    print("Verifying source folder...")
    if os.path.exists(source_path):
        print("Source folder exists. Verification successful.\n")
        print("Initiating file copy...")
        recursive_folder_copy(source_path, dest_path) # copy function
        print("File copy complete.")
    else:
        raise Exception(f"Source directory '{source_path}' missing.\nCanceling operation.")
    
    
    print("Operation complete.")