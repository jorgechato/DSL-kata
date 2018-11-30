# DSL Kata

Python solution uses a different approach because the language lacks a block syntax and multi-line lambdas.
Each of these objects is built inline using readable method names.

This implementation overloads the operators `==`, `!=`, `>` and `<` for operations on the text and range fields.

```python
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

# out

<form id='adidas-form'>
<label>User Name<label/>
<input name='user' size='140' label='User Name' type='text'/>
<form/>
-----
<form id='adidas-form'>
<label>User Name<label/>
<input name='user' size='140' label='User Name' type='text'/>

<label>Password<label/>
<input label='Password' type='password'/>
<form/>
```

## Run

```bash
$ python main.py
```

## Strengths

- Single step for creating the request
- Easy to dynamically create criteria
- Operator overloading improves readability

## Weaknesses

- Repetition of the class name
- Literal list used as argument

## TL;DR

In general, there are 3 types of DSL implementations: `fluent interface`, `readable inline method arguments` and `blocks`.
Fluent interfaces is the most effective approach for the static languages.
For Python, readable inline method arguments seemed to be the most idiomatic.
