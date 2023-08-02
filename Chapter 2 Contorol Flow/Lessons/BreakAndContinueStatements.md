# Break and continue statements

In Python, the `break` and `continue` statements are used to control the flow of a loop.

The `break` statement is used to exit a loop prematurely, regardless of whether the loop condition has been met or not. When the `break` statement is encountered inside a loop, the loop immediately terminates and control is transferred to the next statement after the loop.

For example, let's use a `while` loop to print the numbers from 1 to 5, but break out of the loop when we reach the number 3:

```python
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
```

Output:
```
1
2
3
```

In this example, we use a `while` loop to print the numbers from 1 to 5. Inside the loop, we use an `if` statement to check if the current value of `i` is equal to 3. If it is, we use the `break` statement to exit the loop prematurely. As a result, only the numbers 1, 2, and 3 are printed.

The `continue` statement is used to skip the current iteration of a loop and move on to the next iteration. When the `continue` statement is encountered inside a loop, the remaining statements inside the loop for the current iteration are skipped, and control is transferred to the next iteration of the loop.

For example, let's use a `for` loop to print the even numbers from 1 to 10, but skip the number 6:

```python
for i in range(1, 11):
    if i == 6:
        continue
    if i % 2 == 0:
        print(i)
```

Output:
```
2
4
8
10
```

In this example, we use a `for` loop to iterate over the numbers from 1 to 10. Inside the loop, we use an `if` statement to check if the current value of `i` is equal to 6. If it is, we use the `continue` statement to skip the current iteration of the loop and move on to the next iteration. As a result, the number 6 is skipped and only the even numbers (2, 4, 8, and 10) are printed.

Both the `break` and `continue` statements are useful for controlling the flow of a loop and making your code more efficient. However, it's important to use them carefully and avoid creating infinite loops or other unintended behavior.