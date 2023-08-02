# Python Operators

Operators in Python are symbols or keywords used to perform operations on one or more values. Python has several types of operators, including:

## Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations on numeric values. Here are some examples:

```python
x = 10
y = 6

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus (returns the remainder after division)
print(x ** y)  # Exponentiation (raises x to the power of y)
print(x // y)  # Floor Division (returns the integer result of division)
```

## Assignment Operators

Assignment operators are used to assign a value to a variable. They also perform an operation on the variable at the same time. Here are some examples:

```python
x = 10
x += 5  # Same as x = x + 5
print(x)

y = 6
y -= 3  # Same as y = y - 3
print(y)

z = 3
z *= 2  # Same as z = z * 2
print(z)
```

## Comparison Operators

Comparison operators are used to compare two values and return a Boolean value (True or False) based on the result. Here are some examples:

```python
x = 10
y = 6

print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to
print(x == y)  # Equal to
print(x != y)  # Not equal to
```

## Logical Operators

Logical operators are used to combine two or more Boolean expressions and return a Boolean value. Here are some examples:

```python
x = 10
y = 6
z = 3

print(x > y and y > z)  # And (returns True if both expressions are True)
print(x > y or y < z)   # Or (returns True if either expression is True)
print(not(x > y))       # Not (returns the opposite of the expression)
```

## Membership Operators

Membership operators are used to test if a sequence (such as a string, list, or tuple) contains a specific value. Here are some examples:

```python
x = "Hello, World!"

print("Hello" in x)   # In (returns True if the specified value is present in the sequence)
print("Goodbye" not in x)  # Not In (returns True if the specified value is not present in the sequence)
```

These are the basic types of operators in Python, but there are also other operators that are used for more advanced programming tasks.