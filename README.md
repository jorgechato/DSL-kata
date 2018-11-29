# DSL Kata

<!-- Python solution uses a different approach because the language lacks a block syntax and multi-line lambdas. -->
<!-- The search method expects a list of objects representing search criteria. -->
Each of these objects is built inline using readable method names.
<!-- The search method is then able to iterate over the provided objects to build the search request. -->

<!-- This implementation overloads the operators `==`, `!=`, `>` and `<` for operations on the text and range fields. -->

```python
print(
	Form(CharField(name=”user”,size=”25”,label=”ID”), id=”myform”)
)

<form id='myform'>
	<label>ID</label>
	<input type='text' name='name' size='25'/>
	<br/>
</form>
```

## Strengths

<!-- - Single step for creating the request and performing the search -->
- Easy to dynamically create criteria
- Operator overloading improves readability

## Weaknesses

<!-- - Repetition of the class name -->
- Literal list used as argument

## TL;DR

In general, there are 3 types of DSL implementations: `fluent interface`, `readable inline method arguments` and `blocks`.
Fluent interfaces is the most effective approach for the static languages.
For Python, readable inline method arguments seemed to be the most idiomatic.
