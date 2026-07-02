import unittest
from extract import extract_markdown_images

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/zjjcJKZ2.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/zjjcJKZ2.png"),
            ],
            matches
        )