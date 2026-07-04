from htmlnode import HTMLNode
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from blocktypes import block_to_block_type, BlockType
from leafnode import LeafNode
from text_to_textnode import text_to_textnode
from textnode import TextNode, TextType, text_node_to_html_node

def text_to_children(text: str) -> list[LeafNode]:
    broken = text_to_textnode(text)
    together = []
    for piece in broken:
        together.append(text_node_to_html_node(piece))

    return together

def markdown_to_html_node(markdown_text) -> HTMLNode:


    """
    Convert markdown text to an HTML node.

    Args:
        markdown_text (str): The markdown text to convert.

    Returns:
        str: The HTML representation of the markdown text.
    """
    markdown_blocks = markdown_to_blocks(markdown_text)
   
    html_nodes = []

    for block in markdown_blocks:
        block=block.replace("\n", "",1)
        if  block_to_block_type(block) == BlockType.PARAGRAPH:
            block=block.replace("\n", " ")
            html_nodes.append(ParentNode("p", text_to_children(block)))
        elif block.startswith("######"):
            html_nodes.append(ParentNode("h6", text_to_children(block)))
        elif block.startswith("#####"):
            html_nodes.append(ParentNode("h5", text_to_children(block)))
        elif block.startswith("####"):
            html_nodes.append(ParentNode("h4", text_to_children(block)))
        elif block.startswith("###"):
            html_nodes.append(ParentNode("h3", text_to_children(block)))
        elif block.startswith("##"):
            html_nodes.append(ParentNode("h2", text_to_children(block)))
        elif block.startswith("#"):
            html_nodes.append(ParentNode("h1", text_to_children(block)))
        elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
            html_nodes.append(ParentNode("ul", text_to_children(block)))
        elif block_to_block_type(block) == BlockType.ORDERED_LIST:
            html_nodes.append(ParentNode("ol", text_to_children(block)))
        elif block_to_block_type(block) == BlockType.CODE:
            code = TextNode("<code>"+block.strip("```")+"</code>", TextType.CODE)
            html_nodes.append(LeafNode("pre", code.text,))    
    

        
    parent = ParentNode("div", html_nodes)


    return parent

    

