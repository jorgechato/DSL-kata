from dsl.base import Form
from dsl.base import CharField
from dsl.base import PasswordField

print("Form")

print("="*5)

print(
    Form(CharField(name="user", size="140", label="User Name"), id="adidas-form")
)

print("-"*5)

print(
    Form(
        CharField(name="user", size="140", label="User Name"),
        PasswordField(label="Password"),
        id="adidas-form",
    )
)
