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
        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading 1</h1><h3>Heading 3 with <i>emphasis</i></h3><h6>Heading 6</h6></div>"
            )

    def test_markdown_to_html_node_unordered_list(self):
        md = """
* Item 1 is **bold**
* Item 2 is *italic*
* Item 3 is `code`
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), 
            "<div><ul><li>Item 1 is <b>bold</b></li><li>Item 2 is <i>italic</i></li><li>Item 3 is <code>code</code></li></ul></div>"
            )

    def test_markdown_to_html_node_ordered_list(self):
        md = """
1. Item 1 is **important**
2. Item 2 is *special*
3. Item 3 is `unique`
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), 
            "<div><ol><li>Item 1 is <b>important</b></li><li>Item 2 is <i>special</i></li><li>Item 3 is <code>unique</code></li></ol></div>"
            )

    def test_markdown_to_html_node_quote(self):
        md = """
>This is a quote
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), 
            "<div><blockquote>This is a quote</blockquote></div>"
            )

    def test_markdown_to_html_node_code_multiline(self):
        md = """
```This is code.
This is a second line of code.
This is a third line of code.```
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), 
            "<div><pre><code>This is code.\nThis is a second line of code.\nThis is a third line of code.</code></pre></div>"
            )

    def test_markdown_to_html_node_paragraph_multiline(self):
        md = """
This is a paragraph
with multiple lines.

This is another paragraph.
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), 
            "<div><p>This is a paragraph\nwith multiple lines.\nThis is another paragraph.</p></div>"
            )