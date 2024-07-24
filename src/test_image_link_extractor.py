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
        matches = extract_images("This is text with a ![image](https://i.imgur.com/aKaOqIh.gif)")
        self.assertListEqual([("image", "https://i.imgur.com/aKaOqIh.gif")], matches)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_default(self):
        matches = extract_links("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)")
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )