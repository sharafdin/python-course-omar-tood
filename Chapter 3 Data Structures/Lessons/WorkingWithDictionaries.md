# Dictionaries in Python

Dictionaries are a built-in data structure in Python that allow you to store and retrieve data using key-value pairs. In this lesson, we will cover the basics of working with dictionaries in Python.

## Creating a Dictionary

To create a dictionary in Python, use curly braces `{}` and separate the keys and values with a colon `:`. For example:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
```

In this example, `my_dict` contains three key-value pairs: `"name": "Sharafdin"`, `"age": 34`, and `"planet": "Jupiter"`.

## Accessing Values

You can access the value associated with a key in a dictionary using square brackets `[]` and the key name. For example:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
print(my_dict["age"]) # prints 34
```

If the key does not exist in the dictionary, you will get a `KeyError`:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
print(my_dict["gender"]) # raises KeyError: 'gender'
```

To avoid this error, you can use the `get()` method, which returns `None` if the key is not found:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
print(my_dict.get("gender")) # prints None
```

## Modifying Values

You can modify the value associated with a key in a dictionary by assigning a new value to the key:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
my_dict["age"] = 31
print(my_dict) # prints {"name": "Sharafdin", "age": 31, "planet": "Jupiter"}
```

## Adding and Removing Key-Value Pairs

You can add a new key-value pair to a dictionary by assigning a value to a new key:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
my_dict["gender"] = "Male"
print(my_dict) # prints {"name": "Sharafdin", "age": 34, "planet": "Jupiter", "gender": "Male"}
```

You can remove a key-value pair from a dictionary using the `del` keyword:

```python
my_dict = {"name": "Sharafdin", "age": 34, "planet": "Jupiter"}
del my_dict["planet"]
print(my_dict) # prints {"name": "Sharafdin", "age": 34}
```

## Conclusion

Dictionaries are a powerful and flexible data structure in Python that allow you to store and retrieve data using key-value pairs. By understanding how to create, access, modify, and iterate over dictionaries, you can become a more effective Python programmer.