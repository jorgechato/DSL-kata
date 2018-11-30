from dsl.base import Form
from dsl.base import CharField

print("Form")

print("="*5)

print(
    Form(CharField(name="user", size="140", label="User Name"), id="adidas-form")
)
