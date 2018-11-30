from dsl.html import HtmlElement
from dsl.html import InputElement

print("Input label")

print("="*5)

print(
    InputElement(name="name")
)

print("-"*5)

print(
    InputElement(name="name", label="User name")
)
