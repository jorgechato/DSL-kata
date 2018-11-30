from dsl.element import Input

print("Input label")

print("="*5)

print(
    Input(name="name")
)

print("-"*5)

print(
    Input(name="name", label="User name")
)
