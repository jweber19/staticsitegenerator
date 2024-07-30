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
        parts = []
        extractions = extract_links(old_node.text)
        print(f"extractions: {extractions}")
        # iterate over the number of link-url tuples in extractions, split and append to parts list
        for i in range(len(extractions)):
            #print(f"i is: {i}")
            #print(f"extraction string: [{extractions[i][0]}]({extractions[i][1]})")
            split_pair = old_node.text.split(f"[{extractions[i][0]}]({extractions[i][1]})", 1)
            #print(f"split_pair: {split_pair}")
            for split in split_pair:
                if split is not "":
                    parts.append(split)
                #print(f"append parts list: {parts}")
        
        # iterate over length of split parts and inject link url in textnode appended to new nodes alternating text and link by odd and even position.
        """
        for i in range(len(parts)):
            if i % 2 == 0:
                link = extractions[i][i]
                url = extractions[i][1]

                new_nodes.append(TextNode(parts[i], text_type_text))
                new_nodes.append(TextNode(link, text_type_link, url))
            else:
                link = extractions[i][i]
                url = extractions[i][1]

                new_nodes.append(TextNode(parts[i], text_type_text))
                new_nodes.append(TextNode(link, text_type_link, url))
        """
        return None #new_nodes
        """
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



        ======================================================================================================
        One link and url in one TextNode text string
        =================================================
        Link/Url Strings
            link_1 = extractions[0][0]
            url_1 = extractions[0][0]
        
        Current split string elements
            - 
        
        Goal
            allow for strings to contain 1 or > 1 links and addresses in a text string.
            purpose: 
                - to properly handle link and url extractions
                - to properly handle textnode creation

        Need
            a list containing 1st element of split_1 and split 2
            a way to inject link and url into textnode via iteration through extracted tuple list

        Pseudocode Ideas
            - 


        ======================================================================================================
        Two links and urls in one TextNode text string
        =================================================
        Link/Url Strings
            link_1 = extractions[0][0]
            url_1 = extractions[0][1]
            link_2 = extractions[1][0]
            url_2 = extractions[1][1]]
        
        Current split string elements
            split_1 = ['This is text with a link ', ' and [to youtube](https://www.youtube.com/@bootdotdev)']
            split_2[0] = [' and ', '']
        
        Goal
            

        Need
            a list containing 1st element of split_1 and split 2
            a way to inject link and url into textnode via iteration through extracted tuple list

        Pseudocode Ideas
            
        """