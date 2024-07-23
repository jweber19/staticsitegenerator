import re

def extract_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links