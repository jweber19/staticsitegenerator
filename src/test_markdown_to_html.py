import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node_heading(self): # 3 cases: generic, inline md, max heading length
        md = """
# Heading 1
### Heading 3 with *emphasis*
###### Heading 6
"""

        node = markdown_to_html_node(md)
    """
        self.assertEqual(
            node.to_html(),
            "<h1>Heading 1</h1>",
            "<h3>Heading 3 with <b>emphasis</b></h3>",
            "<h6>Heading 6</h6>",
        )
    """

    def test_markdown_to_html_node_unordered_list(self): # 3 cases: generic, inline md, max heading length
        md = """
* UL Item 1 is **bold**
* UL Item 2 is *italic*
* UL Item 3 is `code`
"""
        node = markdown_to_html_node(md)
    """
        self.assertEqual(
            node.to_html(),
            "<tag>content</tag>",
            "<tag>content</tag>",
            "<tag>content</tag>",
        )
    """

    def test_markdown_to_html_node_ordered_list(self): # 3 cases: generic, inline md, max heading length
        md = """
1. OL Item 1 is **bold**
2. OL Item 2 is *italic*
3. OL Item 3 is `code`
"""
        node = markdown_to_html_node(md)
    """
        self.assertEqual(
            node.to_html(),
            "<tag>content</tag>",
            "<tag>content</tag>",
            "<tag>content</tag>",
        )
    """