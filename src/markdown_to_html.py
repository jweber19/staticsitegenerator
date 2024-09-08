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

# process heading blocks
def process_heading(block):
    heading_count = len(block) - len(block.lstrip("#"))
    block_text = block.strip("#")
    block_text = block_text.strip()
    textnodes = text_to_textnodes(block_text)
    html_nodes = [text_node_to_html_node(node) for node in textnodes] # list comprehension
    return ParentNode(f"h{heading_count}", html_nodes)

# process unordered lists
def process_unordered_list(block):
    html_nodes = []

    lines = block.split("\n")
    items = []
    current_item = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("*") or stripped_line.startswith("-"):
            if current_item: # empty list = "falsy", non-empty list = "truthy".
                items.append('\n'.join(current_item))
                current_item = []
        current_item.append(line)
    if current_item:
        items.append('\n'.join(current_item))

    for item in items:
        item_text = item.lstrip("-* ")
        item_text = item_text.strip()
        textnodes = text_to_textnodes(item_text)
        #print(f"\ntextnode: {textnodes}")
    #print(f"\nTextnodes Type: {type(textnodes)}")
    return ParentNode("ul", html_nodes)

# process ordered lists
def process_ordered_list(block):
    pass

# process quote blocks
def process_quote(block):
    pass

# process code blocks
def process_code(block):
    pass

# process paragraph blocks
def process_paragraph(block):
    pass

# call appropriate block processor for each type
def block_processor(block, block_type):
    if block_type == block_type_heading:
        html_node = process_heading(block)
        return html_node
    if block_type == block_type_unordered_list:
        html_node = process_unordered_list(block)
        return html_node
    if block_type == block_type_ordered_list:
        #process_ordered_list(block)
        pass
    if block_type == block_type_quote:
        #process_quote(block)
        pass
    if block_type == block_type_code:
        #process_code(block)
        pass
    if block_type == block_type_paragraph:
        #process_paragraph(block)
        pass
    else:
        print(f"\nunknown block type: {block_type}")
        input("press enter to continue")


# main function
def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_processor(block, block_type)
        html_nodes.append(html_node)
    
    root_node = ParentNode("div", html_nodes)

    print(f"\n{root_node.to_html()}")