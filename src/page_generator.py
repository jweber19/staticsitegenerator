import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

# global variables for single file testing purposes
from_path = ""
template_path = ""
dest_path = ""

def generate_page(from_path, template_path, dest_path):
    
    # setup paths and confirm existence
    current_directory = os.getcwd()
    from_path = os.path.join(current_directory, "content", "index.md")
    template_path = os.path.join(current_directory, "template.html")
    dest_path = os.path.join(current_directory, "public", "index.html")
    if os.path.exists(from_path):
        print("From path found.")
    else:
        print("Error. From path does not exist. Skipping for now.")
    if os.path.exists(dest_path):
        print("Destination path found.")
    else:
        print("Error. 'Destination Path' does not exist. Skipping for now.")
    if os.path.exists(template_path):
        print("Template path found.")
    else:
        print("Error. Template path does not exist. Skipping for now.")
    
    # gather necessary files for html generation
    print(f"\nGenerating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template_html = f.read()
    node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    generated_html = node.to_html()
    
    # inject generated html into template
    output_html = template_html.replace("{{ Title }}", title)
    output_html = output_html.replace("{{ Content }}", generated_html)
    print(output_html)
    # return (output_html)

def main():
    generate_page(from_path, template_path, dest_path)
main()