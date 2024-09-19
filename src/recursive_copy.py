import os, shutil

#path = "test_path_dir"
source_path = "static"
dest_path = "public"

def main():
    #if os.path.exists(path): # verify if a string exists as a path in the cd
    #    print(f"success! {path}")
    #else:
    #    print("fail")

    #if os.listdir(path): # return any directories as a string
    #    dir = os.listdir(path)
    #    path_list = []
    #    for d in dir:
    #        new_path = ""
    #        new_path = os.path.join(path, d) # concatenate two strings into a path separated by a '/'
    #        path_list.append(new_path)
    #print(path_list)
    #else:
    #    print("no directories found")
    
    #print(os.path.isfile(path)) # return true if the path variable is a file
    #print(os.path.isdir(path)) # return true if the path variable is a folder
    
    #os.mkdir(path) # creates a directory in the path
    
    #shutil.copy(dst, src) # copy files from a source to a destination
    #shutil.rmtree # delete an entire directory tree - path must point to a directory
    
    # check if public path exists
    # if yes shutil.rmtree public path
    # else return error: destination path not found

    # check if static path exists
    # if yes copy files from static path to public path
        # for each file print each path to the screen
    # else return error source path not found
    
    print(f"Cleaning destination path '{dest_path}'")
    shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    print("\nComplete.")
    input("Check if public folder cleaned.\nPress any key to continue...")
    print(f"\nCopying from local source folder '{source_path}' to local destination folder '{dest_path}'.")
    os.listdir(source_path)
    dir = os.listdir(source_path)
    for d in dir:
        source_content_path = ""
        dest_content_path = ""
        source_content_path = os.path.join(source_path, d)
        dest_content_path = os.path.join(dest_path, d)
        # if source content path is folder
            # if not folder dest content path (folder source content path)
                # mkdir in dest content path
        # if source content path is file
            # if not file dest content path (file source content path)
                # shutil.copy

        print(f"\nCopying... {source_content_path}")
        shutil.copy(dest_content_path, source_content_path)
    print("Complete.")

main()