import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_block_type(self):
        md = """
# This is a heading    
## This is also a heading
###### This is the last heading

- Line 1 of an unordered list
- Line 2 of an unordered list

1. Line 1 of an ordered list
2. Line 2 of an ordered list

This is **bolded** paragraph,
This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line

>This Is A\n>Multi Line\n>Quote
        """
        markdown_to_html_node(md)