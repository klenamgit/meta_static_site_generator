from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    """Enum for Text types."""
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    ANCHOR = "anchor"
    IMAGE = "images"
    LINK = "links"
    TEXT = "text"

class TextNode:
    """Class for TextNode."""
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="strong", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="em", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url, "alt": text_node.text})
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    else:
        raise ValueError("Unknown type")