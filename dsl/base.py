from dsl.element import Html
from dsl.element import Input


class Form(Html):
    tag = "form"


class CharField(Input):
    default_attributes = {"type": "text"}


class EmailField(CharField):
    pass


class PasswordField(Input):
    default_attributes = {"type": "password"}
