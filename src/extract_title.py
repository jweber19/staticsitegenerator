from markdown_blocks import block_to_block_type
from markdown_to_html import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            heading_count = len(block) - len(block.lstrip("#"))
            if heading_count == 1:
                block = block.strip("#")
                title = block.strip()
                return title
            else:
                raise Exception("file missing <h1> header")