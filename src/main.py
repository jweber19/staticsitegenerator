from page_generator import generate_page
from recursive_copy import recursive_copy

def main():
    source_path = "static"
    dest_path = "public"
    from_path = "content/index.md"
    template_path = "template.html"

    recursive_copy(source_path, dest_path)
    generate_page(from_path, dest_path, template_path)

main()