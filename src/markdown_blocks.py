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
    if re.match(r"^#{1,6}\s(?! )(.*)", markdown):
        return "heading"
    if re.match(r"^```(.*)```$", markdown):
        return "code"
    if not re.findall(r"^(?!>).", markdown, flags=re.MULTILINE):
        return "quote"
    if not re.findall(r"^(?![-*] ).", markdown, flags=re.MULTILINE):
        return "unordered list"
    if markdown.startswith("1. "):
        lines = markdown.split("\n")
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered list"
    else:
        return "paragraph"
    
