import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is bold text", text_type_bold)
        new_node = split_nodes_delimiter([node], "*", text_type_bold)
        print(f"Test: Bold - {new_node}")
        
    def test_delim_bold_double(self):
        pass

    def test_delim_bold(self):
        pass


if __name__ == "__main__":
    unittest.main()