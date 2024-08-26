"""
    This function file will process full markdown text files into html nodes.
    It will use markdown block conversion functions as well as html node class objects to achieve this.
"""

from htmlnode import(
    HTMLNode,
    LeafNode,
    ParentNode,
)

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
    pass