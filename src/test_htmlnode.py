import unittest
from htmlnode import HTMLNode

#Testing if props to html works correctly
#put nothing in node, put everything but node, only node
class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("div", "class = container", [HTMLNode("p", "", ["Hello, World!"])], {"id": "main"})
        node2 = HTMLNode("div", "class = container", [HTMLNode("p", "", ["Hello, World!"])], {"id": "main"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_props_to_html(self):
        node = HTMLNode("div", "class = container", [HTMLNode("p", "", ["Hello, World!"])], {"id": "main"})
        expected = ' id="main"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode("div", "class = container", [HTMLNode("p", "", ["Hello, World!"])])
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
