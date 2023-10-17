# Python Functions

Functions in Python allow you to encapsulate reusable blocks of code and execute them whenever needed. They make your code more modular and organized.

## Function Definition

To define a function in Python, you use the def keyword followed by the function name and parentheses. Here's an example of a function definition that prints "Hello, world!" when called:

```python
def greet():
    print("Hello, world!")
```    


## Function Invocation

To call or invoke a function, you simply use its name followed by parentheses. Here's an example of calling the greet function defined above:

```python
greet()
```

This will ```print "Hello, world!```.

## Function Parameters

Functions can accept parameters, allowing you to pass values into the function for it to work with. Here's an example:

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Omar")
```

In this example, the greet function takes a parameter called name. When calling the function, we provide the value "Alice" as an argument.

## Return Values

Functions can also return values using the return statement. Here's an example:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

In this example, the add function takes two parameters, a and b, and returns their sum using the return statement.



# *args and **kwargs in Python

In Python, *args and **kwargs are used to handle variable-length arguments in function definitions.

## *args (Positional Arguments)

The *args syntax allows a function to accept a variable number of positional arguments. It collects all extra positional arguments passed to the function as a tuple.

Example:
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15

```
## **kwargs (Keyword Arguments)

The **kwargs syntax allows a function to accept a variable number of keyword arguments. It collects all extra keyword arguments passed to the function as a dictionary.

### Example:
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

print_info(name="Omar", age=25, city="Mogadishu")
```

You can use *args and **kwargs together in a function definition to handle both positional and keyword arguments.

```python
def example_function(*args, **kwargs):
    # Use args and kwargs as needed
    pass
```

By using *args and **kwargs, you can create functions that accept a flexible number of arguments and provide more dynamic behavior.

Remember to place the parameter definitions in the following order: required parameters, *args, **kwargs.



# Function Scope in Python

- Variables defined outside functions have global scope.
- Variables defined inside functions have local scope.
- Local variables are accessible only within the function.
- Global variables can be accessed from anywhere in the program.
- Local variables can shadow global variables with the same name.
- Use the global keyword to modify global variables within a function.

Example:
```python
global_var = 10

def my_function():
    local_var = 20
    print(global_var)
    print(local_var)

my_function()  # Output: 10, 20

```



Maximum Numbers Finding Program:

```python 
def find_maximum(*numbers):
    if len(numbers) == 0:
        return None

    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum

numbers_list = [15, 7, 42, 23, 10]
maximum_number = find_maximum(*numbers_list)
print("The maximum number is:", maximum_number)
```



# Example Password Length:

``` python
def check_password_length(password, min_length):
    if len(password) >= min_length:
        return True
    else:
        return False

password = input("Enter your password: ")
minimum_length = 8

if check_password_length(password, minimum_length):
    print("Password meets the minimum length requirement.")
else:
    print("Password does not meet the minimum length requirement.")

``` 

# Example get Age:

```python
 def age_teller():
    current_year = 2023  
    birth_year = int(input("Enter your birth year: "))
    age = current_year - birth_year

    if age < 0:
        print("Invalid birth year. Please try again.")
    elif age > 150:
        print("You seem to be too old to use this system.")
    else:
        print(f"You are {age} years old.")

# Example usage
age_teller()

```

# Example Calculate grade.

``` python

def calculate_total_grade(grades):
    total = sum(grades)
    return total

# Example usage
grades = [85, 90, 78, 92, 88]
total_grade = calculate_total_grade(grades)
print(f"Total grade: {total_grade}")

```


# Example Payment System.

``` python
balance = 0.0

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposit of {amount} successful. Current balance: {balance}")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Withdrawal of {amount} successful. Current balance: {balance}")
    else:
        print("Insufficient funds. Withdrawal unsuccessful.")

def get_balance():
    return balance


# Example usage
def perform_payment():
    deposit(100.0)  # Deposit of 100.0 successful. Current balance: 100.0
    withdraw(50.0)  # Withdrawal of 50.0 successful. Current balance: 50.0
    withdraw(75.0)  # Insufficient funds. Withdrawal unsuccessful.
    current_balance = get_balance()
    print(f"Current balance: {current_balance}")  # Current balance: 50.0


perform_payment()

```


