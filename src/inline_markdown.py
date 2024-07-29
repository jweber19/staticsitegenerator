from image_link_extractor import extract_images, extract_links
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
        
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            print("appending something...not text") # debug
            continue
        
        parts = []
        extractions = extract_links(old_node.text) # result is a list with 2 tuples each with 2 elements representing link/url pair inside.
        print(f"link extractions: {extractions}") # [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        print(f"setting up first link/url split parameter...")
        link_1 = extractions[0][0] # extracts 1st tuple element in 1st list item
        url_1 = extractions[0][1] # extracts 2nd tuple element in 1st list item
        print(f"link: {link_1}") # 'to boot dev'
        print(f"url: {url_1}") # 'https://www.boot.dev'
        split_1 = old_node.text.split(f"[{link_1}]({url_1})", 1) # splits sentence before and after string including link and url
        parts.append(split_1[0])
        print(f"splitting node '{old_node.text}'") # 'This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)'
        print(f"split 1 result: {split_1}") # ['This is text with a link ', ' and [to youtube](https://www.youtube.com/@bootdotdev)']

        print(f"setting up next link/url split parameter...")
        link_2 = extractions[1][0] # extracts 1st tuple element in 2nd list item
        url_2 = extractions[1][1] # extracts 2nd tuple element in 2nd list item
        print(f"link: {link_2}") # 'to youtube'
        print(f"url: {url_2}") # 'https://www.youtube.com/@bootdotdev'
        print(f"searching split_1 list for next link url split parameter...")
        for item in split_1:
            if f"[{link_2}]({url_2})" in item: # skips items in the split list that don't contain the split parameter string
                print(f"found split parameter!")
                print(f"splitting node '{item}...'") # 'and [to youtube](https://www.youtube.com/@bootdotdev)'
                split_2 = item.split(f"[{link_2}]({url_2})", 1) # splits target string containing parameter by parameter string
        parts.append(split_2[0])
        print(f"split 2 result: {split_2}") # [' and ', '']
    

        for i in range(len(parts)):
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], text_type_text))
                new_nodes.append(TextNode(link_1, text_type_link, url_1))
            else:
                new_nodes.append(TextNode(parts[i], text_type_text))
                new_nodes.append(TextNode(link_2, text_type_link, url_2))
        
        return new_nodes



        """
        Link/Url Strings
            link_1 = extractions[0][0]
            url_1 = extractions[0][0]
            link_2 = extractions[0][0]
            url_2 = extractions[0][0]
        
        Current split string elements
            split_1 = ['This is text with a link ', ' and [to youtube](https://www.youtube.com/@bootdotdev)']
            split_2[0] = [' and ', '']
        
        Goal
            set up conditionals to sequentially and accurately create TextNode objects for each, alternating types text or link and injecting link and url objects

        Need
            a list containing 1st element of split_1 and split 2
            a way to inject link and url into textnode via iteration through extracted tuple list

        Pseudocode Ideas
            parts = ['This is text with a link ', 'and ']
            
            
            temp_nodes = [] # list to carry TextNodes

            for i in range(len(list))
                if i % 2 == 0:
                    temp_nodes.append(TextNode(parts[i], text_type_text)
                    temp_nodes.append(TextNode(link_1, text_type_link, url_1))
                else:
                    temp_nodes.append(TextNode(parts[i], text_type_text)
                    temp_nodes.append(TextNode(link_2, text_type_link, url_2))
 
        """