import re
def extract_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    print(f"initial text: {text}")
    links = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return links