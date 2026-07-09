---
layout: page
title: "Lesson 5: Strings"
permalink: /lessons/05-strings/
---

## Introduction

### What this lesson is about

A *string* is a sequence of characters — basically any text.  This lesson covers
how to create strings, combine them, extract parts of them, and use Python's
rich set of built-in string methods to manipulate text.

### Why you need this

Data rarely arrives in exactly the right format.  Student names have inconsistent
capitalisation, spreadsheet entries have trailing spaces, and values need to be
formatted for display or saved to files.  String manipulation is therefore an
everyday Python skill.

---

## Do

### Step 1 — Creating strings

Strings can use single quotes, double quotes, or triple quotes:

```python
name = "Alice"
subject = 'Mathematics'
note = """This is a
multi-line string."""
```

Use triple quotes for text that spans more than one line.

1) Create a new file called `strings.py` in the `resources/lesson-05` directory.
2) Add the code from the examples above to the file.
3) Add print statements to print the values of the variables.

---

### Step 2 — Concatenation and repetition

```python
first = "Hello"
second = "World"
message = first + ", " + second + "!"

line = "-" * 30
```

1) Add the code from the examples above to the file.
2) Add print statements to print the values of the variables. What do you notice?

---

### Step 3 — f-strings (formatted string literals)

f-strings let you embed values directly inside a string — by far the most
readable way to build strings from variables:

```python
name = "Alice"
score = 87
print(f"{name} scored {score}%")           # Alice scored 87%
print(f"{name} scored {score:.1f}%")       # Alice scored 87.0%
print(f"Double her score: {score * 2}")    # Double her score: 174
```

1) Add a function that takes a name and score as parameters and returns a formatted string using an f-string.  Remember functions should go above statements in the file.
2) Call the function with different values and print the result.

---

### Step 4 — String methods

Python strings come with many built-in methods:

```python
text = "  Hello, World!  "

print(text.strip())          # "Hello, World!"   — remove whitespace
print(text.upper())          # "  HELLO, WORLD!  "
print(text.lower())          # "  hello, world!  "
print(text.replace("World", "Python"))   # "  Hello, Python!  "
print(text.strip().startswith("Hello"))  # True
print(text.strip().endswith("!"))        # True

 ```

1) Write a function that accepts a string and returns it with leading and trailing whitespace removed, and all characters converted to lowercase.
2) Call the function with different values and print the result.
   - Example: `process_text("  Hello, World!  ")` should return `"hello, world!"`

---

### Step 5 — Splitting and joining

```python
csv_line = "Alice,87,A"
parts = csv_line.split(",")

# Join a list back into a string
rejoined = " | ".join(parts)
print(rejoined)        # Alice | 87 | A
```

This example uses a list data type which has not been covered yet, but it demonstrates the concept of joining a list of strings into a single string.

1) Write a function that takes a CSV line (like "Alice,87,A") and returns a formatted string with the values separated by dashes (like "Alice - 87 - A").
2) Call the function with 3 different values and print the result.

---

### Step 6 — Indexing and slicing

Strings are sequences — you can access individual characters or sub-strings:

```python
word = "Mathematics"

print(word[0])      # M   — first character (index 0)
print(word[-1])     # s   — last character
print(word[0:4])    # Math, start at index 0 and go up to (but not including) index 4
print(word[4:])     # ematics, start at index 4 and go to the end
print(word[:4])     # Math, start at the beginning and go up to (but not including) index 4
print(word[2:8:2])    # tea, start at index 2 and go up to (but not including) index 8, stepping by 2
print(len(word))    # 11  — number of characters
```

1) Write a function that takes a string and returns the first 3 characters, the last 3 characters, and the length of the string.
2) Call the function with different values and print the result.
3) Use slicing to extract the substring "them" from "Mathematics".

---

### Step 7 — Checking content

```python
sentence = "The quick brown fox"

print("quick" in sentence)        # True
print(sentence.count("o"))        # 2
print(sentence.find("brown"))     # 10  (index where it starts)
```



---

### Step 8 — Converting other types to strings

```python
score = 95
grade = "A*"

# You cannot concatenate a string and an int directly:
# print("Score: " + score)  ← this raises a TypeError

# Convert with str():
print("Score: " + str(score))   # Score: 95

# Or use an f-string:
print(f"Score: {score}, Grade: {grade}")
```
1) Write a function that takes a score and a grade and returns a formatted string with the score and grade.
2) Call the function with different values and print the result.

> **Download:** [strings.py]({{ site.baseurl }}/resources/lesson-05/strings.py)

---

## Explore

1. Write a function `title_case(name)` that converts a full name to title case,
   e.g. `"alice smith"` → `"Alice Smith"`.  Python has a `.title()` method —
   can you find it?
2. A student enters their name as `"  BOB JONES  "`.  Write code to clean it up
   to `"Bob Jones"`.
3. Write a function `initials(full_name)` that returns the initials from a full
   name.  `initials("Alice Mary Smith")` should return `"A.M.S."`.
4. How would you check whether a string represents a whole number?  Look up the
   `.isdigit()` method.
5. f-strings support format specifiers: `f"{3.14159:.2f}"` gives `"3.14"`.
   Experiment with formatting numbers as percentages, with leading zeros, or
   aligned to a fixed width.

---

[← Lesson 4]({{ site.baseurl }}/lessons/04-docstrings/)
[Next Lesson: Text Files →]({{ site.baseurl }}/lessons/06-text-files/)
