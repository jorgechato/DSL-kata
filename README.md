# DSL Kata

Python solution uses a different approach because the language lacks a block syntax and multi-line lambdas.
Each of these objects is built inline using readable method names.

This implementation overloads the operators `__str__` for operations on the text and range fields.

```python
print(
    Input(name="name")
)

print(
    Input(name="name", label="User name")
)
```

```html
<label>name<label/>
<input name='name'/>

<label>User name<label/>
<input name='name' label='User name'/>
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
