import re
def markdown_to_blocks(markdown):
    temp_string = ""
    blocks = []

    parts = markdown.split('\n')
    for part in parts:
        if part != "":
            temp_string += (f"{part}"'\n')
        else:
            if temp_string.strip():
                blocks.append(temp_string.strip())
                temp_string = ""
    return blocks

def block_to_block_type(markdown):
    if markdown == re.match(r"(#+)('')(.*?)", markdown):
        return "heading"
    #if markdown == x:
        #return "code"
    #if markdown == x:
        #return "quote"
    #if markdown == x:
        #return "unordered_list"
    #if markdown == x:
        #return "ordered_list"
    else:
        return "paragraph"
    
