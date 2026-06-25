from unittest import TestCase
from leafnode import LeafNode

class TestLeafNode(TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode(tag="p",value="Hello, World!", props={"class": "text"})
        expected_html = '<p class="text">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self):
        node = LeafNode(value="Hello, World!")
        expected_html = 'Hello, World!'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_none_value(self):
        node = LeafNode(tag="p", props={"class": "text"})
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_to_html_with_h1_tag(self):
        node = LeafNode(value="Hello, World!", tag="h1", props={"class": "text"})
        expected_html = '<h1 class="text">Hello, World!</h1>'
        self.assertEqual(node.to_html(), expected_html)
    def test_repr(self):
        node = LeafNode(value="Hello, World!", tag="p", props={"class": "text"})
        expected_repr = "LeafNode(value=Hello, World!, tag=p, props={'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)