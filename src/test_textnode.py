import unittest
from text_node_to_html_node import text_node_to_html_node
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
from htmlnode import LeafNode
from inline_markdown import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    """
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)
    
    def test_text_ineq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is another text node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_text_type_ineq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)
    
    def test_url_ineq(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_italic, "https://www.google.ca")
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    
    
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is text", text_type_text)
        html_node = text_node_to_html_node(text_node)
        formatted_html_node = html_node.to_html()
        print(f"{formatted_html_node}")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(text_node)
        formatted_html_node = html_node.to_html()
        print(f"{formatted_html_node}")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is italic", text_type_italic)
        html_node = text_node_to_html_node(text_node)
        formatted_html_node = html_node.to_html()
        print(f"{formatted_html_node}")
    
    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is code", text_type_code)
        html_node = text_node_to_html_node(text_node)
        formatted_html_node = html_node.to_html()
        print(f"{formatted_html_node}")

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("This is an image", text_type_image, "url/of/image.jpg")
        html_node = text_node_to_html_node(text_node)
        formatted_html_node = html_node.to_html()
        print(f"{formatted_html_node}")
    
    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Click Here!", text_type_link, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        formatted_html_node = html_node.to_html()
        print(f"{formatted_html_node}")
    
    """
    def test_split_nodes_delimiter(self):
        node = TextNode("This is a text with a `code` block word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        print(f"new nodes: {new_nodes}")

if __name__ == "__main__":
    unittest.main()