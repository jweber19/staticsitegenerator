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

# get delimiter
def get_delimiter(block_type):
    if block_type == block_type_heading:
        return heading
    if block_type == block_type_unordered_list:
        return unordered_list
    if block_type == block_type_ordered_list:
        return ordered_list
    if block_type == block_type_quote:
        return quote
    if block_type == block_type_code:
        return code
    else:
        return ""

# strip markdown from blocks via delimiter
def md_strip(block, block_type):
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


def block_to_lines(block):
    if '\n' in block:
        line = block.split('\n')

        for line in block:
            block_lines = block_lines.append(line)
        return block_lines
    
    else:
        return block


def block_to_text(block, block_type):


# return a list of child leafnodes
def text_to_children(text):
    children = [] # set up list to hold leafnodes
    textnodes = text_to_textnodes(text) # convert from text to textnode
    for node in textnodes:
        leafnode = text_node_to_html_node(node) # convert each textnode to an html leafnode
        children.append(leafnode)
    return children



# filter block types and process accordingly
def block_to_textnodes(block, block_type):
    children = text_to_children(block) # convert any block inline md to child nodes
    parentnode = ParentNode("p", children) # set up parentnode object and inject child list
    return parentnode
    

# main function behavior
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # separate md string block into \n separated blocks

    for block in blocks:
        block_type = block_to_block_type(block) # get block type
        block_lines = block_to_lines(block) # separate blocks into lines
        textnodes = block_to_textnode(block_lines, block_type)

        htmlnode = block_to_textnodes(block, block_type)
        
        if htmlnode is not None:   # skip empty blocks, temporary: change once all if switches are complete
           print (htmlnode.to_html()) # convert the node to html and print to screen
           # return htmlnode # return the node to be compared for accuracy
        