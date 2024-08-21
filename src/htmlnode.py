# The HTMLNode class represents a node in an HTML doc tree and will render itself as HTML.
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # this is a string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dict of key-value pairs repr the attr of the HTML tag. E.g. a link (<a> tag) might have {"href": "https://www.google.com"}

    def to_html(self): # Child classes will override this method to render themselves as HTML.
        raise NotImplementedError("to_html method not implemented") # this is a common way to imply the function is abstract and will be used by child class objects.

    def props_to_html(self): # returns a string representing the HTML attr of the node.
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self): # a method for debugging that will print to the screen and allow you to see the tag, value, children and props.
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode): # A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. 
                          # We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. It's a node with no children.
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self): # renders the leaf node as an HTML string. 
        if self.value is None:
            raise ValueError("Invalid HTML: no value") # needs a value by definition.
        if self.tag is None:
            return self.value # if there is no tag the value will be rendered as raw text
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode): # Handles the nesting of HTML nodes inside each other. Parent nodes are HTML nodes with children = non-leaf nodes. 
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: # requires a tag
            raise ValueError("Invalid HTML: no tag")
        if self.children is None: # requires children
            raise ValueError("Invalid HTML: no children")
        
        # recursive code that will nest child nodes inside the parent node.
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"