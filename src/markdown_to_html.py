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

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"
block_type_quote = "quote"


def block_to_htmlnode(block_type, block):
    if block_type == block_type_paragraph:
        print(f"block type paragraph\n{block}\n")
    if block_type == block_type_heading:
        print(f"block type heading\n{block}\n")
    if block_type == block_type_unordered_list:
        print(f"block type unordered list\n{block}\n")
    if block_type == block_type_ordered_list:
        print(f"block type ordered list\n{block}\n")
    if block_type == block_type_quote:
        print(f"block type quote\n{block}")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    print("\n")
    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = block_to_htmlnode(block_type, block)