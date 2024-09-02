import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_block_to_html_node(self):
        md = """
# GitHub

It's a **great** website where you can effectively manage *version control*

## Also
"""
        node = markdown_to_html_node(md)
"""
        self.assertEqual(
            node.to_html(),
            "<p>It's a <b>great</b> website where you can effectively manage <i>version control</i></p>",
        )
"""