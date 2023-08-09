# Function Scope in Python

Scope refers to where variables are accessible:
- **Local Scope**: Inside functions, variables are local.
- **Global Scope**: Outside functions, variables are global.

## Local Scope

Variables within functions are only accessible inside the function itself.

Example:
```python
def my_function():
    x = 10
    print(x)

my_function()  # Output: 10
```

## Global Scope

Variables defined outside functions are accessible everywhere.
Use `global` to modify global variables within functions.

Example:
```python
y = 20

def another_function():
    global y
    y = y + 1
    print(y)

another_function()  # Output: 21
print(y)  # Output: 21
```

Understanding scope helps prevent bugs and manage variable access in your code. Local scope isolates data, while global scope provides broader access.