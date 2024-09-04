import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_block_to_html_node(self):
        md = """
# GitHub

It's a **great** website where you can effectively manage *version control.* Check out the website here [github.com](https://github.com/)
![bootdev](https://www.boot.dev/img/bootdev-logo-full-small.webp)

## Also

>This is a quote.

### Next

```print("Hello World!)```

#### Forthrightly

* Item 1: Do not forget.
* Item 2: Nor this one.
* Item 3: Nayther this.

##### Lastly

1. Buy eggs
2. Drink Milk
3. Eat Bacon
"""
        node = markdown_to_html_node(md)
"""
        self.assertEqual(
            node.to_html(),
            "<p>It's a <b>great</b> website where you can effectively manage <i>version control</i></p>",
        )
"""