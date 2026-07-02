from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    one = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            return new_nodes
        if old.text.count(delimiter) != 2:
            raise Exception("There is no closing delimiter")
        else:
            index = old.text.index(delimiter)
            one.extend(old.text.split(delimiter))
            new_nodes = [TextNode(one[0],TextType.TEXT),TextNode(one[1],text_type),TextNode(one[2], TextType.TEXT)]
    return new_nodes

