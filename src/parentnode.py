from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    """A ParentNode is a node that can have children."""
    def __init__(self, tag: str, children: list, props: dict[str, str] = None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        
        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode")
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"