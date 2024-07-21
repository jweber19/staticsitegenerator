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
    for node in old_nodes:
        if node.text_type == "text": # only split text type nodes
            parts = node.text.split(delimiter) # splits the text elem in the 1st node 

            if len(parts) % 2 == 0: # checks for odd split count = no delim match
                raise ValueError(f"Unmatched delimiter '{delimiter}' found in text: {node.text}")

            for i, part in enumerate(parts): # enumerate to keep order
                if i % 2 == 0:
                    # even index -> original text type
                    node = TextNode(part, node.text_type)
                else:
                    # odd index -> new text type
                    node = TextNode(part, text_type)
                new_nodes.append(node)
        else:
            new_nodes.append(node) # avoids splitting non_text nodes

    return new_nodes