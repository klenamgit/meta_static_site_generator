import unittest
from text_to_textnode import text_to_textnode

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **bold** and _italic_ and `code` and ![image](https://example.com/image.png) and [link](https://example.com)"
        expected_nodes = [
            ("This", "text", None),
            ("is", "text", None),
            ("bold", "bold", None),
            ("and", "text", None),
            ("italic", "italic", None),
            ("and", "text", None),
            ("code", "code", None),
            ("and", "text", None),
            ("image", "images", "https://example.com/image.png"),
            ("and", "text", None),
            ("link", "links", "https://example.com")
        ]
        
        result_nodes = text_to_textnode(text)
        
        for result_node, expected in zip(result_nodes, expected_nodes):
            self.assertEqual(result_node.text, expected[0])
            self.assertEqual(result_node.text_type.value, expected[1])
            self.assertEqual(result_node.url, expected[2])