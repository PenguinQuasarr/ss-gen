import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):

        # Test One
        node_one = HTMLNode()
        self.assertEqual(node_one.props_to_html(), "")

        # Test Two
        node_two = HTMLNode(tag="p", value="greeting", props={"id": "greeting"})
        self.assertEqual(node_two.props_to_html(), "id=greeting ")

        # Test Three
        node_three = HTMLNode(
            "h1", "Welcome", [], {"style": "color: red; background-color: black"}
        )
        self.assertEqual(
            node_three.props_to_html(), "style=color: red; background-color: black "
        )


if __name__ == "__main__":
    unittest.main()
