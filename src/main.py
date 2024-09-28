from page_generator_recursive import generate_page_recursive
from recursive_copy import recursive_copy

def main():
    source_path = "static" # important files c
    dest_path = "public" # output folder
    from_path = "content" # markdown content
    template_path = "template.html" # html template for generator

    recursive_copy(source_path, dest_path)
    generate_page_recursive(from_path, dest_path, template_path)
    
main()