"""
    This function file will process full markdown text files into html nodes.
    It will use markdown block conversion functions as well as html node class objects to achieve this.
"""

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

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"
block_type_quote = "quote"


def block_to_textnodes(block_type, block):
    if block_type == block_type_paragraph: # process paragraph blocks
        textnodes = text_to_textnodes(block)
        """
        for node in textnodes:
            print(node) # debug output
            Output:
TextNode(It's a , text, None)
TextNode(great, bold, None)
TextNode( website where you can effectively manage , text, None)
TextNode(version control, italic, None)
TextNode(Check out my GitHub page, link, https://github.com/jweber19)
            """
        return textnodes
    if block_type == block_type_heading: # process heading blocks
        pass
    if block_type == block_type_unordered_list: # process unordered list blocks
        pass
    if block_type == block_type_ordered_list: # process ordered list blocks
        pass
    if block_type == block_type_quote: # process quote blocks
        pass


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # separate md string block into \n separated blocks
    #print("\n") # debugging
    textnode_count = 0 # used to count block iterations for clearer debugging output formatting
    print('\n') # debug output formatting
    for block in blocks: # iterate over block list
        block_type = block_to_block_type(block) # get block type from markdown_blocks
        textnodes = block_to_textnodes(block_type, block) # convert blocks using if switches to list of textnodes (see above function)

        if textnodes is not None:   # skip empty blocks, temporary: change once all if switches are complete
            textnode_count += 1 # used to count block iterations for clearer debugging output formatting
            print(textnode_count) # used to count block iterations for clearer debugging output formatting

            for node in textnodes:  # loop over each textnodes list
                htmlnode = text_node_to_html_node(node)     # convert each textnode to an html node. recursive function for children?
                print(htmlnode) # debugging
            print('\n') # used to separate iterations for clearer debugging output

            """Output:

1
LeafNode(None, It's a , None)
LeafNode(b, great, None)
LeafNode(None,  website where you can effectively manage , None)
LeafNode(i, version control, None)


2
LeafNode(a, Check out my GitHub page, {'href': 'https://github.com/jweber19'})


"""