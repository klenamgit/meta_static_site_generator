from textnode import TextNode, TextType


def text_to_textnode(text: str) -> list[TextNode]:
    """
    take is a string split it accoring to text types
    create text nodes for it with the text type
    list all split function
    split_nodes_image(
    split_nodes_delimiter(
    split_nodes_link(
    This is **text** with an _italic_ word and 
    a `code block` and an 
    ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)
      and a [link](https://boot.dev)
loop the string
look of "**", "_", "`", "![", "["

appending to the text
    """
    new_nodes = []
    for word in text.split():
        if word.startswith("**") and word.endswith("**"):
            new_nodes.append(TextNode(word[2:-2], TextType.BOLD))
        elif word.startswith("_") and word.endswith("_"):
            new_nodes.append(TextNode(word[1:-1], TextType.ITALIC))
        elif word.startswith("`") and word.endswith("`"):
            new_nodes.append(TextNode(word[1:-1], TextType.CODE))
        elif word.startswith("![") and "](" in word and word.endswith(")"):
            alt_text = word[2:word.index("](")]
            url = word[word.index("]")+2:-1]
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
        elif word.startswith("[") and "](" in word and word.endswith(")"):
            link_text = word[1:word.index("](")]
            url = word[word.index("]")+2:-1]
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
        else:
            new_nodes.append(TextNode(word, TextType.TEXT))
    return new_nodes   

