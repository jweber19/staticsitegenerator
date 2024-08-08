def markdown_to_blocks(markdown):
    temp_string = ""
    blocks = []

    parts = markdown.split('\n')
    if part in parts != "":
      temp_string += (f"{part}"'\n')
      else:
            block_list.append(temp_string)
            temp_string = ""
    if temp_string:
      block_list.append(temp_string.strip())
    return block_list
