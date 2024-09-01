import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_block_to_html_node(self):
        md = """
# GitHub

It's a **great** website where you can effectively manage *version control*

## Also

- It's easy to use
- Super popular

[Check out my GitHub page](https://github.com/jweber19)
"""
        markdown_to_html_node(md)

