class HtmlElement():
    default_attributes = {}
    tag = "unknown_tag"

    def __init__(self, *args, **kwargs):
        self.attributes = kwargs
        self.attributes.update(self.default_attributes)
        self.children = args

    def __str__(self):
        attribute_html = " ".join([
            "{}='{}'".format(
                name, value
            ) for name, value in self.attributes.items()
        ])

        if not self.children:
            return "<{} {}/>".format(self.tag, attribute_html)
        else:
            children_html = "".join([
                str(child) for child in self.children
            ])

            return "<{} {}>{}<{}/>".format(
                self.tag,
                attribute_html,
                children_html,
                self.tag
            )


class InputElement(HtmlElement):
    tag = "input"

    def __init__(self, *args, **kwargs):
        HtmlElement.__init__(self, *args, **kwargs)
        self.label = self.attributes[
            "label"
        ] if "label" in self.attributes else self.attributes["name"]

        if "label" in self.attributes.items():
            del self.attributes["label"]

    def __str__(self):
        label_html = "<label>{}<label/>\n".format(self.label)

        return label_html + HtmlElement.__str__(self)
