import sys

# import class objects and other functions
from htmlnode import(
    HTMLNode,
    LeafNode,
    ParentNode,
)
from textnode import(
    TextNode,
    text_node_to_html_node,
)
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
)
from text_processor import (
    text_to_textnodes,
)

# create block type references
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"
block_type_quote = "quote"
block_type_image = "image"
block_type_code = "code"

# create block type delimiters
heading = "#"
unordered_list = "-* "
ordered_list = "1234567890. "
quote = ">"
code = "```"


"""
# strip markdown from blocks via delimiter
def remove_markdown(block, block_type):

    
    if block_type == block_type_ordered_list:
        new_block_line = ""
        stripped_block = ""
        split_blocks = block.split('\n')
        for block in split_blocks:
            new_block_line = block.strip(get_delimiter(block_type)) # strip md by number and period
            if new_block_line.strip():
                stripped_block += (f"{new_block_line}\n") # missing newline reinsertion
        return stripped_block
    else:
        if '\n' in block:
            new_block = ""
            blocks = block.split("\n")
            for line in blocks:
                temp_string = ""
                temp_string += (line.strip(get_delimiter(block_type)))
                if temp_string.strip():
                    new_block += (f"{temp_string}\n")
            return new_block
        else:
            block = block.strip(get_delimiter(block_type)) # strip md
            new_block = block.strip() # strip remaining whitespace
            return new_block
"""
# process heading blocks
def process_heading(block):
    heading_count = len(block) - len(block.lstrip("#")) # get accurate heading '#' count starting from left side
    print(f"\nheading_count: {heading_count}")
    print(f"\nblock: {block}")
    block_text = block.strip("#")
    print(f"block_text: {block}")
    block_text = block_text.strip()
    print(f"block_text.strip: {block_text}")
    response = input("program paused...")
    return None
    # create html node
    # return html node

# process unordered lists
def process_unordered_list(block):
    pass

# process ordered lists
def process_ordered_list(block):
    pass

# process quote blocks
def process_quote(block):
    pass

# process code blocks
def process_code(block):
    pass

# call appropriate block processor for each type
def block_processor(block, block_type):
    if block_type == block_type_heading:
        process_heading(block)
    if block_type == block_type_unordered_list:
        process_unordered_list(block)
    if block_type == block_type_ordered_list:
        process_ordered_list(block)
    if block_type == block_type_quote:
        process_quote(block)
    if block_type == block_type_code:
        process_code(block)
    else:
        raise ValueError("Block type processing error")


# main function
def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_processor(block, block_type)
        html_nodes = html_nodes.append(html_node)
    
    root_node = HTMLNode("div", html_nodes)

    print(root_node.to_html())