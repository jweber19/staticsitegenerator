from page_generator import generate_page
from recursive_copy import recursive_copy

def main():
    source_path = "static" # important files c
    dest_path = "public" # output folder

    from_path = "content" # markdown content
    template_path = "template.html" # html template for generator

    recursive_copy(source_path, dest_path) # cleans dest_path folder and recursively copies source_path contents for use in generator
    generate_page(from_path, dest_path, template_path) # generates html using template in from_path
    
main()