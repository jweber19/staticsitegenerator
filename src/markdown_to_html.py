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

# create delimiters
heading = "#"



# strip markdown from blocks via delimiter
def md_strip(block, delimiter):
    block = block.strip(delimiter) # strip md
    new_block = block.strip() # strip remaining whitespace
    return new_block



# return a list of child leafnodes
def text_to_children(text):
    children = [] # set up list to hold leafnodes
    textnodes = text_to_textnodes(text) # convert from text to textnode
    for node in textnodes:
        leafnode = text_node_to_html_node(node) # convert each textnode to an html leafnode
        children.append(leafnode)
    return children



# filter block types and process accordingly
def block_to_textnodes(block_type, block):

    if block_type == block_type_paragraph: # process paragraph blocks
        children = text_to_children(block) # convert any block inline md to child nodes
        parentnode = ParentNode("p", children) # set up parentnode object and inject child list
        return parentnode
    
    if block_type == block_type_heading: # process heading blocks
        heading_count = block.count("#") # get heading count
        stripped_block = md_strip(block, heading) # remove md from heading text
        children = text_to_children(stripped_block)
        parentnode = ParentNode(f"h{heading_count}", children)
        return parentnode
    """
    if block_type == block_type_unordered_list: # process unordered list blocks
        pass
    if block_type == block_type_ordered_list: # process ordered list blocks
        pass
    if block_type == block_type_quote: # process quote blocks
        pass
    if block_type == block_type_code: # process code blocks
        pass
    """

# main function behavior
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # separate md string block into \n separated blocks
    print('\n')
    for block in blocks: # iterate over block list
        block_type = block_to_block_type(block) # get block type from markdown_blocks
        htmlnode = block_to_textnodes(block_type, block) # convert blocks using if switches to list of textnodes (see above function)
        
        if htmlnode is not None:   # skip empty blocks, temporary: change once all if switches are complete
           print (htmlnode.to_html()) # convert the node to html and print to screen
           # return htmlnode # return the node to be compared for accuracy
        