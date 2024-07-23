import unittest
from image_link_extractor import (
    extract_images,
    extract_links,
)
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)

class TestExtractImages(unittest.TestCase):
    
    def test_default(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_node = extract_images(node.text)
        print(f"image test: {new_node}")
    
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_default(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        new_node = extract_links(node.text)
        print(f"link test: {new_node}")
    
