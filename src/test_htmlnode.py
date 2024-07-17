import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
"""
class TestHTMLNode(unittest.TestCase):
    # tests all parameters
    def test_all_html(self):
        node = HTMLNode("a", "Click me!", ["p", "b"], {"href": "https://www.google.com"})
        print(f"props test: {node.props_to_html()}")
        print(f"repr test: {node.__repr__()}")

    # tests only tag
    def test_tag(self):
        node = HTMLNode("tag test", None, None, None)
        print(f"props tag only test: {node.props_to_html()}")
        print(f"repr tag only test: {node.__repr__()}")
    
    # tests only props
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
        print(f"props only test: {node.props_to_html()}")
        print(f"props only repr test: {node.__repr__()}")

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        try:
            leaf1 = LeafNode("p", "This is a paragraph.") # tests tag and value
            leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) # tests tag, value, props
            leaf3 = LeafNode(None, "This is a paragraph.") # tests for value rendered as text
            leaf4 = LeafNode("a", None, {"href": "https://www.google.com"}) # tests tag and props for no value

            print(leaf1.to_html())
            print(leaf2.to_html())
            print(leaf3.to_html())
            print(leaf4.to_html())
        except ValueError as ve:
            print(f"Caught exception: {ve}")
    
class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        children_test = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ]
        
        nested_node_test = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        ParentNode(
                            "span",
                            [
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text inside span"),
                            ]
                        ),
                    ]
                ),
                LeafNode("h1", "Header text"),
            ]
        )

        no_children_test = ParentNode("div", [],)

        try:
            parent_node1 = ParentNode("p", children_test)

            print(parent_node1.to_html())
            print(nested_node_test.to_html())
            print(no_children_test.to_html())
        
        except ValueError as ve:
            print(f"Caught exception: {ve}")
        
        #print(parent_node1.__repr__())
        #print(nested_node_test.__repr__())
        #print(no_children_test.__repr__())
"""
if __name__ == "__main__":
    unittest.main()