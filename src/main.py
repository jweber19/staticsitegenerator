from recursive_copy import recursive_copy

def main():
    source_path = "static"
    dest_path = "public"
    recursive_copy(source_path, dest_path)
    
main()