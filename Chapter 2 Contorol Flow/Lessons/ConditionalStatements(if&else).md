# Conditional Statements (if/elif/else)

In Python, conditional statements are used to make decisions based on certain conditions. The most common type of conditional statement is the `if/elif/else` statement.

## The `if` Statement

The `if` statement is used to check if a condition is true. If the condition is true, the code inside the `if` block is executed. For example:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

In this example, we're checking if `x` is greater than 5. If the condition is true, the code inside the `if` block is executed, which prints "x is greater than 5".

## The `elif` Statement

The `elif` statement is used to add additional conditions to check if the first condition is false. If the first condition is false and the `elif` condition is true, the code inside the `elif` block is executed. For example:

```python
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 10:
    print("x is greater than 10 but less than or equal to 15")
```

In this example, we're checking if `x` is greater than 15 or greater than 10 but less than or equal to 15. If `x` is greater than 15, the first condition is true and the code inside the `if` block is executed. If `x` is not greater than 15 but is greater than 10, the second condition is true and the code inside the `elif` block is executed.

## The `else` Statement

The `else` statement is used to provide code to execute if all the previous conditions are false. For example:

```python
x = 5

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")
```

In this example, we're checking if `x` is greater than 10, greater than 5 but less than or equal to 10, or less than or equal to 5. If `x` is greater than 10, the first condition is true and the code inside the `if` block is executed. If `x` is not greater than 10 but is greater than 5, the second condition is true and the code inside the `elif` block is executed. If both conditions are false, the code inside the `else` block is executed.

## Example

For example, let's say we want to write a program that checks if a number is even or odd. We can use an `if/else` statement to do this:

```python
number = 10

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

In this example, we're checking if `number` is divisible by 2 with no remainder. If the condition is true, the code inside the `if` block is executed, which prints "The number is even". If the condition is false, the code inside the `else` block is executed, which prints "The number is odd".

The `if` statement is followed by a condition. If the condition is true, the code inside the `if` block is executed. If the condition is false, the code inside the `else` block is executed.

You can also add additional conditions with the `elif` keyword. For example:

```python
number = 10

if number < 0:
    print("The number is negative")
elif number == 0:
    print("The number is zero")
else:
    print("The number is positive")
```

In this example, we're checking if `number` is negative, zero, or positive. If `number` is less than 0, the first condition is true and the code inside the `if` block is executed. If `number` is equal to 0, the second condition is true and the code inside the `elif` block is executed. If neither condition is true, the code inside the `else` block is executed.