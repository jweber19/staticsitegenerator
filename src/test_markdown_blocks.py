import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_simple(self):
        test_markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        test_markdown_result = markdown_to_blocks(test_markdown)
        #print(test_markdown_result)
        self.assertEqual(
            test_markdown_result,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_blocktype_heading(self):
        md = "# This Is a Heading"
        block_type = block_to_block_type(md)
        #print(block_type)
        self.assertEqual(block_type, "heading")
    
    def test_blocktype_paragraph(self):
        md = "This is **bolded** paragraph"
        block_type = block_to_block_type(md)
        #print(block_type)
        self.assertEqual(block_type, "paragraph")