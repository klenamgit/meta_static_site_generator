from recursive_move import get_files
import os

from generate_page import generate_page
def generate_pages_recursive(dir_path_content,template_path, dest_dir_path):
    crawl = get_files(dir_path_content)
    print(crawl)
    for file in crawl:
        if file[-3:]==".md":
            generate_page(file,template_path, os.path.join(dest_dir_path,file.replace(".md",".html")))