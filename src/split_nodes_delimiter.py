from textnode import TextNode
"""
Input
"This is a text with a 'code' block word"

Return
[
    TextNode("This is text with a ", "text"),
    TextNode("bolded phrase", "bold"),
    TextNode(" in the middle", "text"),
]
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type, ):
    
    return