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
from inline_markdown import (
    split_nodes_delimiter, 
    split_nodes_images, 
    split_nodes_links
    )

class TestInlineMarkdown(unittest.TestCase):
    """
    def test_delim_bold_single(self):
        node = TextNode("This is a text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
       
    def test_delim_bold_double(self):
        node = TextNode("This is a text with **two****bold** words", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is a text with ", text_type_text),
                TextNode("two", text_type_bold),
                TextNode("bold", text_type_bold),
                TextNode(" words", text_type_text),
            ],
            new_nodes,
        )
    
    def test_delim_bold_multiword(self):
        node = TextNode("This is a **multi word** secondary **bold** test", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("multi word", text_type_bold),
                TextNode(" secondary ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" test", text_type_text),
            ],
            new_nodes,
        )
    
    def test_delim_italic(self):
        node = TextNode("This is an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is a text with a `code` block word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" block word", text_type_text),
            ],
            new_nodes,
        )
    """

    def test_split_node_images(self):
        pass

    def test_split_node_link(self):
        node = TextNode( 
            "This is a text with a link [to boot dev](https://www.boot.dev)",
            text_type_text
        )
        new_nodes = split_nodes_links([node])
        print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is a text with a link ", text_type_text),
                TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_node_links(self):
        node = TextNode( 
            "This is a text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text
        )
        new_nodes = split_nodes_links([node])
        print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is a text with a link ", text_type_text),
                TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()