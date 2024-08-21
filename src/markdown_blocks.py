import re

# takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings.
# blocks in final list have had any leading and trailing whitespace stripped from them.
# A 'block' is considered a single line or multiple sequential lines. Empty new lines in between are removed. 
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

# takes a single block of markdown text as input and returns a string representing the type of block it is.
# block types include: paragraph, heading, code, quote, unordered_list, ordered_list
def block_to_block_type(markdown):
    if re.match(r"^#{1,6}\s(?! )(.*)", markdown): # Heading = '#(1-6) Heading Text'
        return "heading"
    if re.match(r"^```(.*)```$", markdown): # Code = '```Code Text```'
        return "code"
    if not re.findall(r"^(?!>).", markdown, flags=re.MULTILINE): # Quote = '>Quote Text'
        return "quote"
    if not re.findall(r"^(?![-*] ).", markdown, flags=re.MULTILINE): # Unordered List = '- List' or '* List' on 1 or < lines
        return "unordered list"
    if markdown.startswith("1. "): # Ordered list = '1. List entry one' and or '2. List entry two' and so on.
        lines = markdown.split("\n")
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered list"
    else:
        return "paragraph" # Paragraph = 'Anything that is not the above examples.'
    
