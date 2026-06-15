---
layout: page
title: "Lesson 2: Functions"
permalink: /lessons/02-functions/
---

## Introduction

**What this lesson is about**

A *function* is a named, reusable block of code.  Instead of writing the same
instructions over and over, you define them once and *call* the function whenever
you need it.  This lesson covers the `def` keyword, how to pass information into
a function using *arguments*, how to get information back out using a *return
value*, and the `pass` keyword that acts as a placeholder.

**Why you need this**

Functions are the single most important tool for keeping code organised and easy
to maintain.  Almost every Python program you will ever write contains functions.
Understanding them thoroughly makes all subsequent lessons much easier.

---

## Do

### Step 1 — Defining a simple function

Create a new file called `functions.py` in your `~/crash-py` folder.

```python
def greet():
    print("Hello from inside a function!")
```

This defines a function called `greet` but does **not** run it yet.  To run it,
you must *call* it:

```python
def greet():
    print("Hello from inside a function!")

greet()
```

Run the script:

```bash
python3 functions.py
```

---

### Step 2 — Arguments

Arguments let you pass values *into* a function so it can use them.

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")
```

You can define multiple arguments separated by commas:

```python
def add(a, b):
    print(a + b)

add(3, 5)   # prints 8
add(10, 2)  # prints 12
```

---

### Step 3 — Return values

Instead of printing inside the function you can *return* a value so the caller
can use it.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print("The answer is", result)
```

The `return` statement sends a value back to whoever called the function.
Execution of the function stops at `return`.

```python
def is_even(n):
    return n % 2 == 0   # returns True or False

print(is_even(4))   # True
print(is_even(7))   # False
```

---

### Step 4 — The `pass` keyword

Sometimes you want to define a function as a *placeholder* — you know you will
need it, but you have not written the body yet.  Python requires at least one
statement inside a function body, so you use `pass`:

```python
def calculate_area():
    pass   # TODO: write this later

def calculate_perimeter():
    pass
```

`pass` does nothing; it is simply a valid, empty statement that satisfies
Python's syntax rules.

---

### Step 5 — Named (keyword) arguments

You can call a function using argument *names* instead of relying on position.
This makes code much more readable:

```python
def describe_triangle(base, height):
    area = 0.5 * base * height
    print("Base:", base, "Height:", height, "Area:", area)

# positional — order matters
describe_triangle(6, 4)

# keyword — order does not matter
describe_triangle(height=4, base=6)
```

---

### Step 6 — Putting it together

```python
def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

w = 5
h = 3
print("Area:", rectangle_area(w, h))
print("Perimeter:", rectangle_perimeter(w, h))
```

> **Download:** [functions.py]({{ site.baseurl }}/resources/lesson-02/functions.py)

---

## Explore

1. Write a function called `square` that takes a number and returns its square.
   Test it with `print(square(7))` — you should get `49`.
2. What happens if you call a function *before* it is defined in the file?
   Try it and read the error.
3. Write a function with a *default* argument value, for example
   `def greet(name="World"):`.  What happens when you call `greet()` with no
   argument?
4. Can a function call another function?  Write `double(x)` that returns
   `2 * x`, and then a function `quadruple(x)` that calls `double` twice.
5. What does a function return if it has no `return` statement?  Try
   `result = greet("Alice")` then `print(result)`.

---

[← Lesson 1]({{ site.baseurl }}/lessons/01-installation/)
[Next Lesson: Mathematics →]({{ site.baseurl }}/lessons/03-mathematics/)
