import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, dest_path, template_path):
    # setup paths and confirm existence
    print(f"\nGenerating page from {from_path} to {dest_path} using {template_path}...")
    current_directory = os.getcwd()
    from_path_full = os.path.join(current_directory, from_path)
    template_path_full = os.path.join(current_directory, template_path)
    dest_path_full = os.path.join(current_directory, dest_path, "index.html")
    dest_path_folder = os.path.join(current_directory, dest_path)
    if os.path.exists(from_path_full):
        print("From path found.")
    else:
        raise Exception(f"Error. Missing '{from_path}'.")
    if os.path.exists(dest_path_folder):
        print("Destination path found.")
    else:
        print(f"'{dest_path}' does not exist. Creating folder...")
        os.mkdir(template_path_full)
        print("Done.")
    if os.path.exists(template_path_full):
        print("Template path found.")
    else:
        raise Exception(f"Error. Missing '{template_path}'.")

    # gather necessary files for html generation
    print("\nReading data...")
    with open(from_path_full, 'r') as f:
        markdown = f.read()
    with open(template_path_full, 'r') as f:
        print("Success.")
        template_html = f.read()
    print("Converting Markdown to HTML..")
    node = markdown_to_html_node(markdown)
    print("Success.")
    print("Extracting title...")
    title = extract_title(markdown)
    print("Success.")
    print("Generating HTML...")
    generated_html = node.to_html()
    print("Done.")
    
    # inject generated html into template
    print("Creating HTML file...")
    output_html = template_html.replace("{{ Title }}", title)
    output_html = output_html.replace("{{ Content }}", generated_html)
    print("Done.")
    print("Writing to file...")
    with open(dest_path_full, 'w') as f:
        f.write(output_html)
        print("Finished.")
    print("Operation completed.")