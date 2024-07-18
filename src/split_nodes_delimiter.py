from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type, ):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            parts = node.text.split("`")

            for i, part in enumerate(parts):
                if i % 2 == 0:
                    node = TextNode(part, node.text_type)
                else:
                    node = TextNode(part, text_type)
                new_nodes.append(node)
        else:
            new_nodes.append(node)

    return new_nodes