from textnode import TextNode, TextType
import re
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []
    for old in old_nodes:
        # if old.text_type != TextType.TEXT:
        #     return old_nodes
        # matches = extract_markdown_images(old.text)
        # if matches:
        #     parts = old.text.split(matches[)
        #     count_1 , count_2 = 0, 0
        #     parts.pop(-1)
        #     print(parts)
        #     for i in range(1, len(parts)):
        #         if (i-1) % 2 != 0:
        #             alt_text, link = parts[i-1], parts[i]
        #             count_1 += 1
        #             new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
        #             i += 1
                    
        #         else:
        #             # alt_text, link = matches[count_1][count_2], matches[count_1][count_2+1]
        #             new_nodes.append(TextNode(parts[i-1], TextType.TEXT))
        pattern = r"!\[(.*?)\]\((.*?)\)"
        parts = re.split(pattern, old.text)
        result = [parts[0]]
        for i in range(1, len(parts), 3):
            result.append((parts[i], parts[i + 1]))  # (alt, url) tuple
            result.append(parts[i + 2])
        result.pop(-1)             # text after the image
        for item in result:
            if isinstance(item, tuple):
                new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
            else:
                new_nodes.append(TextNode(item, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old in old_nodes:
        parts = re.split(r'\[([^\]]+)\]\(([^)]+)\)', old.text)
        result = [parts[0]]
        for i in range(1, len(parts), 3):
            result.append((parts[i], parts[i + 1]))  # (alt, url) tuple
            result.append(parts[i + 2])
        result.pop(-1)             # text after the image
        for item in result:
            if isinstance(item, tuple):
                new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
            else:
                new_nodes.append(TextNode(item, TextType.TEXT))
    return new_nodes