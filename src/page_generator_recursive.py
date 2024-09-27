import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

######### inputs passed from main #############################################################
# from_path = "content"                                                    # markdown content #
# dest_path = "public"                                                        # output folder #
# template_path = "template.html"                               # html template for generator #
#                                                                                             #
# from_path:           content                                                                #
# from_path_folder:      /home/deck/github.com/jweber19/staticsitegenerator/content           #
# from_path_file:        /home/deck/github.com/jweber19/staticsitegenerator/content/index.md  #
# dest_path:           public                                                                 #
# dest_path_folder:      /home/deck/github.com/jweber19/staticsitegenerator/public            #
# dest_path_file:        /home/deck/github.com/jweber19/staticsitegenerator/public/index.html #
# template_path:       template.html                                                          #
# template_path_file:    /home/deck/github.com/jweber19/staticsitegenerator/template.html     #
###############################################################################################
"""
TASKS
    1. Crawl every entry in '/content'
    2. For each markdown file found, generate a new .html file using the '/template.html'. 
    3. Write the generated pages to '/public/~' (retain '/content' folder structure)
"""
def generate_page_recursive(from_path, dest_path, template_path):
    # setup paths and confirm existence
    from_path_folder = os.path.join(os.getcwd(), from_path) # = 'content'
    from_path_file = os.path.join(os.getcwd(), from_path, "index.md") # change 'index.md' to a os.getfiles if .md variable
    dest_path_folder = os.path.join(os.getcwd(), dest_path) # = 'public'
    dest_path_file = os.path.join(os.getcwd(), dest_path, "index.html") # change 'index.html' to the original filename variable-
                                                                        # -from before but change the filetype: '.md' to '.html'
    template_path_file = os.path.join(os.getcwd(), template_path) # stays the same

    print(f"\nGenerating page from '/{from_path}' to '/{dest_path}' using '/{template_path}'...")
    # check from path folder exists
    if os.path.exists(from_path_folder):
        print(f"'{from_path_folder}' folder found.")
    else:
        print(f"'{from_path_folder}' folder does not exist. Creating...") # if not, make folder
        os.mkdir(from_path_folder)
        print(f"Writing...'{from_path_folder}'")
        print("Done.")
    # check from path file exists
    if os.path.exists(from_path_file):
        print(f"'{from_path_file}' found.")
    else:
        raise Exception(f"Error. Missing '{from_path_file}'.") # if not raise exception
    # check dest path folder exists
    if os.path.exists(dest_path_folder):
        print(f"'{dest_path_folder}' folder found.")
    else:
        print(f"'{dest_path_folder}' folder does not exist. Creating...") # if not, make folder
        os.mkdir(dest_path_folder)
        print(f"Writing...'{dest_path_folder}'")
        print("Done.")
    # check template file exists
    if os.path.exists(template_path_file):
        print(f"'{template_path_file}' found.")
    else:
        raise Exception(f"Error. Missing '{template_path_file}'.") # if not raise exception

    # gather necessary files for html generation
    #print("\nReading data...")
    with open(from_path_file, 'r') as f:
        markdown = f.read() # load the markdown file into memory
    with open(template_path_file, 'r') as f:
        template_html = f.read() # load the template html into memory
    #print("Converting Markdown to HTML..")
    node = markdown_to_html_node(markdown)
    #print("Success.")
    #print("Extracting title...")
    title = extract_title(markdown)
    #print("Success.")
    #print("Generating HTML...")
    generated_html = node.to_html()
    #print("Done.")
    
    # inject generated html into template
    #print("Creating HTML file...")
    output_html = template_html.replace("{{ Title }}", title)
    output_html = output_html.replace("{{ Content }}", generated_html)
    #print("Done.")
    #print("Writing to file...")
    with open(dest_path_file, 'w') as f:
        f.write(output_html)
    #    print("Finished.")
    #print("Operation completed.")