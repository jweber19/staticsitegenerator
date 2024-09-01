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


"""
class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_block_to_html_node(self):
        md = '''
# GitHub

It's a **great** website where you can effectively manage *version control*

## Also

- It's easy to use
- Super popular

[Check out my GitHub page](https://github.com/jweber19)
'''
        markdown_to_html_node(md)
"""

def block_to_textnodes(block_type, block):
    if block_type == block_type_paragraph: # process paragraph blocks
        children = [] # set up list to hold leafnodes
        textnodes = text_to_textnodes(block) # convert from text to textnodes

        for node in textnodes:  # loop over each textnodes list
            leafnode = text_node_to_html_node(node) # convert each textnode to an html leafnode. recursive function for children?
            children.append(leafnode) # append leafnode to child list
        parentnode = ParentNode("p", children) # set up parentnode object and inject child list
    
        return parentnode
    
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
    print('\n')
    for block in blocks: # iterate over block list
        block_type = block_to_block_type(block) # get block type from markdown_blocks
        htmlnode = block_to_textnodes(block_type, block) # convert blocks using if switches to list of textnodes (see above function)
        if htmlnode is not None:   # skip empty blocks, temporary: change once all if switches are complete
            print(f"{type(htmlnode)}'\n'") # debug
            print(htmlnode.__repr__) # debug