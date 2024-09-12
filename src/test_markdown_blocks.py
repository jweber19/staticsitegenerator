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

######################################################
    # HEADING TESTS
######################################################

    def test_blocktype_heading(self):
        md = "# This Is a Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "heading")
    
    def test_blocktype_heading_excessive_chars(self):
        md = "####### This Is a Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")
    
    def test_blocktype_heading_no_chars(self):
        md = "This Is a Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")


######################################################
    # CODE TESTS
######################################################

    def test_blocktype_code(self):
        md = "```This Is Code```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "code")
    
    def test_blocktype_code_multiline(self):
        md = "```This Is Code\nRight?\nPlease say yes```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "code")
    
    def test_blocktype_code_no_char(self):
        md = "This Is Totally Code"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")
    
    def test_blocktype_code_insufficient_chars(self):
        md = "`This Is Also Totally Code`"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

######################################################
    # QUOTE TESTS
######################################################

    def test_blocktype_quote_single_line(self):
        md = ">This Is A Single Line Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "quote")
    
    def test_blocktype_quote_single_line_no_char(self):
        md = "This Is Not A Single Line Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_blocktype_quote_multi_line_correct(self):
        md = ">This Is A\n>Multi Line\n>Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "quote")
    
    def test_blocktype_quote_multi_line_missing_char(self):
        md = ">This Is\nAn Incorrect\n>Single Line Quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")
    
######################################################
    # UNORDERED LINE TESTS
######################################################

    def test_blocktype_unordered_list_single_line_dash(self):
        md = "- This Is A Single Line Unordered List With a Dash"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "unordered list")
    
    def test_blocktype_unordered_list_single_line_star(self):
        md = "* This Is A Single Line Unordered List With A Star"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "unordered list")
    
    def test_blocktype_unordered_list_single_line_no_char(self):
        md = "This Is Not A Single Line Unordered List With No Dash or Star"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_blocktype_unordered_list_multi_line_correct(self):
        md = "- This Is A Multi Line\n* Unordered List With A Dash And A Star"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "unordered list")
    
    def test_blocktype_unordered_list_multi_line_missing_char(self):
        md = "This Is\nAn Incorrect\nSingle Line Unordered List With No Initial Characters"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

######################################################
    # ORDERED LIST TESTS
######################################################

    def test_blocktype_ordered_list_single_line(self):
        md = "1. This Is An Ordered List With A Single Line."
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "ordered list")

    def test_blocktype_ordered_list_single_line_no_char(self):
        md = "This Is Not An Ordered List With A Single Line."
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_blocktype_ordered_list_triple_line_increment(self):
        md = "1. This Is An\n2. Ordered List With\n3. Incrementally Numbered Lines."
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "ordered list")

    def test_blocktype_ordered_list_triple_line_no_increment(self):
        md = "1. This Is An\nOrdered List With\nNo Incrementally Numbered Lines."
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

######################################################
    # PARAGRAPH TESTS
######################################################

    def test_blocktype_paragraph(self):
        md = "This is **bolded** paragraph"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")