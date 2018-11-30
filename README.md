# DSL Kata

Python solution uses a different approach because the language lacks a block syntax and multi-line lambdas.
Each of these objects is built inline using readable method names.

This implementation overloads the operators `__str__` for operations on the text and range fields.

```python
UserForm
name:CharField -> label:Username size:140
email:EmailField -> size:140
password:PasswordField
```

```html
<form id='userform'>
<label>Username</label>
<input type='text' name='name' size='25'/>

<label>email</label>
<input type='text' name='email' size='32'/>

<label>password</label>
<input type='password' name='password'/>
</form>
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
