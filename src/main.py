import textnode
import recursive_move
from generate_pages_recursive import generate_pages_recursive

def main():
    node = textnode.TextNode("This is some anchor text", "https://www.boot.dev")
    recursive_move.copy_files("static","public")
    generate_pages_recursive("content", "template.html", "public")
    print(node)
    



main()