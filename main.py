from dsl.element import Html

print("Unknown tag")

print("="*5)

print(
    Html(id="yo")
)

print("-"*5)

print(
    Html(
        Html(name="adidas"),
        id="yo",
    )
)
