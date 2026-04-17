from leafnode import LeafNode
from parentnode import ParentNode
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from conversion import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            children.append(ParentNode("p", text_to_children(text)))
        elif block_type == BlockType.HEADING:
            level = len(block) - len(block.lstrip("#"))
            text = block[level + 1 :]
            children.append(ParentNode(f"h{level}", text_to_children(text)))
        elif block_type == BlockType.CODE:
            text = block[4:-3]
            code_node = LeafNode("code", text)
            children.append(ParentNode("pre", [code_node]))
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            text = " ".join(line.lstrip(">").strip() for line in lines)
            children.append(ParentNode("blockquote", text_to_children(text)))
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = [ParentNode("li", text_to_children(line[2:])) for line in lines]
            children.append(ParentNode("ul", items))
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = [
                ParentNode("li", text_to_children(line.split(". ", 1)[1]))
                for line in lines
            ]
            children.append(ParentNode("ol", items))
    return ParentNode("div", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children
