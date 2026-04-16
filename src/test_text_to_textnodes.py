import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_full(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_plain_text(self):
        nodes = text_to_textnodes("This is plain text.")
        self.assertListEqual(
            [
                TextNode("This is plain text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_just_bold(self):
        nodes = text_to_textnodes("This is **bold** text.")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_just_italic(self):
        nodes = text_to_textnodes("This is _italic_ text.")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
            nodes,
        )

    def test_just_code(self):
        nodes = text_to_textnodes("This is a `code block`.")
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )

    def test_just_link(self):
        nodes = text_to_textnodes("This is a [link](https://boot.dev).")
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )

    def test_just_image(self):
        nodes = text_to_textnodes(
            "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)."
        )
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )
