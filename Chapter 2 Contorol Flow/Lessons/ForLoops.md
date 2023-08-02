# For loops
In Python, the for loop is used to iterate over a sequence (such as a list, tuple, or string) and perform a block of code for each item in the sequence.

## Syntax

The basic syntax of a `for` loop in Python is:

```python
for item in sequence:
    # code to be executed for each item
```

Here, `item` is a variable that is used to store the value of the current item in the sequence, and `sequence` is the sequence that is being iterated over.

## Iterating over a sequence

One of the most common uses of a `for` loop in Python is to iterate over a sequence (such as a list, tuple, or string) and perform a block of code for each item in the sequence.

For example, let's say we have a list of numbers and we want to print each number:

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

Output:
```
1
2
3
4
5
```

In this example, the `for` loop iterates over the `numbers` list and assigns each item to the `number` variable. The `print()` function is then used to print each number.

We can also use the `range()` function to generate a sequence of numbers and iterate over them with a `for` loop. For example, let's print the numbers from 0 to 4:

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

In this example, the `range()` function generates a sequence of numbers from 0 to 4, and the `for` loop iterates over each number and prints it.

We can also iterate over a string and perform a block of code for each character in the string. For example, let's print each character in the string "Hello, world!":

```python
string = "Hello, world!"
for character in string:
    print(character)
```

Output:
```
H
e
l
l
o
,
 
w
o
r
l
d
!
```

In this example, the `for` loop iterates over the `string` and assigns each character to the `character` variable. The `print()` function is then used to print each character.

## Nested `for` loops

We can use nested `for` loops to iterate over multiple sequences. For example, let's print all possible combinations of two colors:

```python
colors1 = ["red", "green", "blue"]
colors2 = ["yellow", "orange", "purple"]
for color1 in colors1:
    for color2 in colors2:
        print(color1, color2)
```

Output:
```
red yellow
red orange
red purple
green yellow
green orange
green purple
blue yellow
blue orange
blue purple
```

In this example, the outer `for` loop iterates over the `colors1` list and assigns each color to the `color1` variable. The inner `for` loop iterates over the `colors2` list and assigns each color to the `color2` variable. The `print()` function is then used to print each combination of colors.

## Modifying the sequence during iteration

Sometimes we may want to modify the sequence we are iterating over during the `for` loop. However, we need to be careful when doing this, as it can lead to unexpected behavior.

For example, let's say we want to remove all the vowels from a list of words:

```python
words = ["apple", "banana", "cherry"]
for word in words:
    for letter in word:
        if letter in "aeiou":
            word = word.replace(letter, "")
    print(word)
```

Output:
```
ppl
bnn
chrry
```

In this example, the outer `for` loop iterates over the `words` list and assigns each word to the `word` variable. The inner `for` loop iterates over each letter in the word, and if the letter is a vowel, it is removed from the word using the `replace()` method. The `print()` function is then used to print each modified word.

## Conclusion

In Python, `for` loops are used to iterate over a sequence and perform a block of code for each item in the sequence. We can also use nested `for` loops to iterate over multiple sequences. We need to be careful when modifying the sequence during iteration, as it can lead to unexpected behavior.