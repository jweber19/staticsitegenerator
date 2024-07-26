from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        parts = old_node.text.split(delimiter) # splits the text elem in the 1st old_node 
        if len(parts) % 2 == 0: # checks for odd split count = no delim match
            raise ValueError(f"Invalid markdown formatting: not closed")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], text_type_text))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_images(old_nodes):
    pass

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []
        parts = old_node.text.split("[", 1)
        print(f"parts: {parts}") # debug split result
        split_nodes.append(parts[0])
        print(f"split nodes: {split_nodes}") # debug appended portion

    return new_nodes