from htmlnode import HTMLNode
from textnode import TextNode


def main():
    testNode = TextNode("Test", "link", "https://test.com")
    print(testNode)

    test_html_node = HTMLNode(tag="p", value="greeting")
    print(test_html_node)


main()
