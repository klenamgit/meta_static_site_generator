import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_line(self):
        markdown = "This is a single line."
        expected = ["This is a single line."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_lines(self):
        markdown = "This is the first line.\n This is the second line."
        expected = ["This is the first line.\nThis is the second line."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_lines(self):
        markdown = "This is the first line.\n\nThis is the second line."
        expected = ["This is the first line.", "This is the second line."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_leading_and_trailing_whitespace(self):
        markdown = "  This is the first line. \n  This is the second line.  "
        expected = ["This is the first line.\nThis is the second line."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )  