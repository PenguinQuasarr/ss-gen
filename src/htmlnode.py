class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.childen = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            formatted_response = ""
            for key, value in self.props.items():
                formatted_response += f"{key}={value} "
            return formatted_response

        return ""

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag},value={self.value},children={self.childen},props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return super().__repr__()
