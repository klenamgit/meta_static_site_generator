import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class Testdelimiter(unittest.TestCase):
    def test_normal(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        supposed = [TextNode("This is text with a ", TextType.TEXT),    TextNode("code block", TextType.CODE),    TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, supposed)

    def test_not_text(self):
        node = TextNode("This is text with a ", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        supposed = [TextNode("This is text with a ", TextType.CODE)]
        self.assertEqual(new_nodes, supposed)