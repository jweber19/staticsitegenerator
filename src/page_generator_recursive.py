import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page_recursive(from_path, dest_path, template_path):
    entries = os.listdir(from_path)
    for entry in entries:
        from_path_entry = os.path.join(from_path, entry)
        template_path_entry = os.path.join(template_path)
        if os.path.isfile(from_path_entry):
            dest_path_entry = os.path.join(dest_path, entry.replace(".md", ".html"))
            with open(from_path_entry, 'r') as f:
                markdown = f.read()
            with open(template_path_entry, 'r') as f:
                template_html = f.read()
            node = markdown_to_html_node(markdown)
            title = extract_title(markdown)
            generated_html = node.to_html()
            output_html = template_html.replace("{{ Title }}", title)
            output_html = output_html.replace("{{ Content }}", generated_html)
            with open(dest_path_entry, 'w') as f:
                f.write(output_html)
        else:
            dest_path_folder = os.path.join(dest_path, entry)
            os.mkdir(dest_path_folder)
            generate_page_recursive(from_path_entry, dest_path_folder, template_path)