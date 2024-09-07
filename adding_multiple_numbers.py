"""
To evaluate an expression like "2 + 4 * 5 / 7" in Python, you can use the `eval` function. The `eval` function
parses the expression passed to it and executes Python expression(s) which are written as a string. Here's an example:

```python
expression = "2 + 4 * 5 / 7"
result = eval(expression)
print(result)  # Output: 4.571428571428571
```

In this code, the `eval` function takes the string `expression` and evaluates it as a Python expression. The result
is then printed out.

Please note that using `eval` can be dangerous if you're evaluating expressions from untrusted sources as it can
evaluate any Python code. If you're planning to use this in a real-world application, make sure to sanitize and
validate your inputs to avoid code injection attacks.

If you want to implement a calculator that can parse and evaluate mathematical expressions without using `eval`,
you would need to implement a parser and interpreter. This is a more complex task and goes beyond the scope of a
simple Python script. There are libraries available in Python like `pyparsing` or `lark-parser` that can help with
this task. You might want to look into these if you're interested.

.......................................................

Sure, here's a brief note on the `eval()` function in Python:

- The `eval()` function in Python is a built-in function used to evaluate a string as a Python expression and return the result³.
- It takes a string containing a valid Python expression as input, parses it, and executes the code, ultimately returning the result of the expression³.
- The evaluated expression can be a mathematical operation, a conditional statement, or even a series of function calls⁴.
- The function takes a first argument, called `expression`, which holds the expression that you need to evaluate².
- `eval()` also takes two optional arguments: `globals` and `locals`². These are used to specify the global and local namespace in which the expression is to be evaluated.
- If you pass in a string to `eval()`, then the function parses it, compiles it to bytecode, and evaluates it as a Python expression².
- If you call `eval()` with a compiled code object, then the function performs just the evaluation step².

Please note that using `eval()` can be dangerous if you're evaluating expressions from untrusted sources as it can evaluate any Python code. If you're planning to use this in a real-world application, make sure to sanitize and validate your inputs to avoid code injection attacks².

Source: Conversation with Copilot, 7/22/2024
(1) Python eval() Function - Online Tutorials Library. https://www.tutorialspoint.com/python/python-eval-function.htm.
(2) Understanding Python’s eval() Function (With Examples). https://machinelearningtutorials.org/understanding-pythons-eval-function-with-examples/.
(3) Python eval(): Evaluate Expressions Dynamically – Real Python. https://realpython.com/python-eval-function/.
(4) Python eval() Function - W3Schools. https://www.w3schools.com/python/ref_func_eval.asp.
(5) Python Eval Function. https://www.prepbytes.com/blog/python/python-eval-function/.

"""


get_operands = input('Type your operation here:')

print(eval(get_operands))

