import unittest
from generate_page import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_no_header(self):
        with self.assertRaises(ValueError):
            extract_title("No header here")

    def test_header_two(self):
        with self.assertRaises(ValueError):
            extract_title("## Subheader")

    def test_header_with_extra_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_header_within_text(self):
        self.assertEqual(extract_title("Some text\n# Title\nMore text"), "Title")
