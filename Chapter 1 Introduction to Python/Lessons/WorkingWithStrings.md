In Python, strings are a sequence of characters that can be enclosed in single or double quotes. Here are some examples of working with strings in Python:

1. Concatenating strings:

```python
s1 = "Hello," 
s2 = " world!"
s3 = s1 + s2
print(s3)
```

In this example, we're using the `+` operator to concatenate two strings into a single string.

2. Accessing characters in a string:

```python
s = "Hello, world!"
print(s[0]) # prints the first character of the string
print(s[-1]) # prints the last character of the string
```

In this example, we're using indexing to access individual characters in the string. Indexing in Python starts at 0, so `s[0]` refers to the first character of the string, and `s[-1]` refers to the last character of the string.

3. Slicing a string:

```python
s = "Hello, world!"
print(s[0:5]) # prints the first 5 characters of the string
print(s[7:]) # prints the substring starting from the 7th character of the string
```

In this example, we're using slicing to extract a portion of the string. The syntax for slicing is `[start:end]`, where `start` is the index of the first character to include in the slice, and `end` is the index of the first character to exclude from the slice.

4. f string:

```python
name = "John"
age = 30
print(f"My name is {} and I'm {} years old.")
```

In this example, we're using the `f` string to insert the values of the `name` and `age` variables into the string. The curly braces `{}` are used as placeholders for the variables.

5. Using string methods:

```python
s = "hello, world!"
print(s.upper()) # prints the string in uppercase
print(s.capitalize()) # capitalizes the first character of the string
print(s.replace("world", "Python")) # replaces "world" with "Python" in the string
```

In this example, we're using some built-in string methods to modify the string. The `upper()` method converts the string to uppercase, the `capitalize()` method capitalizes the first character of the string, and the `replace()` method replaces a substring in the string with another substring.