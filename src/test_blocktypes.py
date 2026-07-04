import unittest
from blocktypes import block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_line(self):
        markdown = "This is a single line."
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_heading(self):
        markdown = "# This is a heading"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_code_block(self):
        markdown = "```python\nprint(\'Hello, World!\')"
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_quote(self):
        markdown = "> This is a quote"
        expected = BlockType.QUOTE
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_unordered_list(self):
        markdown = "- This is an unordered list item"
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ordered_list(self):
        markdown = "1. This is an ordered list item"
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_to_block_type(markdown), expected)

    