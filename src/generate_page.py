from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node
import os 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}",from_path, dest_path, template_path)
    with open(from_path, "r") as file:
        content = file.read()
    with open(template_path, "r") as temp:
        temp_content = temp.read()
    
    html = markdown_to_html_node(content)
    work = html.to_html()

    replaced = temp_content.replace("{{ Title }}", extract_title(content))
    replaced = replaced.replace("{{ Content }}", work)
    
    # if os.path.exists(os.path.dirname(dest_path)) == False:
    #         os.makedirs(dest_path)
    os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as save:
         save.write(replaced)