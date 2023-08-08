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