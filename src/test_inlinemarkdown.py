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

    def test_inlinemarkdown(self):
        node = TextNode("This is a text with a `code` block word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        print(f"`Code` Test: {new_nodes}")

    def test_boldsingle(self):
        node = TextNode("This is a text with a *bold* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        print(f"*Bold* Test: {new_nodes}")
       
    def test_bolddouble(self):
        node = TextNode("This is a text with **two** double **bold** words", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        print(f"*2 Double Bold* Test: {new_nodes}")
    

if __name__ == "__main__":
    unittest.main()