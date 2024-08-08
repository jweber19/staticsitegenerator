def markdown_to_blocks(markdown):
    temp_string = ""
    blocks = []

    parts = markdown.split('\n')
    for part in parts:
        if part in parts != "":
            temp_string += (f"{part}"'\n')
        else:
            if temp_string.strip():
                blocks.append(temp_string.strip())
                temp_string = ""
    return blocks
