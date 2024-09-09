import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node_heading(self): # 3 cases: generic, inline md, max heading length
        md = """
# Heading 1
### Heading 3 with *emphasis*
###### Heading 6

* Item 1 is **bold**
* Item 2 is *italic*
* Item 3 is `code`
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




    def test_markdown_block_to_html_node(self):
        md ="""
# GitHub

It's a **great** website where you can effectively manage *version control*. Check out the website here [github.com](https://github.com/)
![bootdev](https://www.boot.dev/img/bootdev-logo-full-small.webp)
    """ 
    
        node = markdown_to_html_node(md)
    """
        self.assertEqual(
            node.to_html(),
            "<p>It's a <b>great</b> website where you can effectively manage <i>version control</i></p>",
        )
    """