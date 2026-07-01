---
layout: page
title: "Lesson 4: Docstrings and Code Documentation"
permalink: /lessons/04-docstrings/
---

## Introduction

Create a new file named `grade.py`


### What this lesson is about

A *docstring* is a string placed immediately after a `def` statement (or at
the top of a module) that describes what the function does.  It is the primary
way Python functions document themselves.  This lesson covers how to write
docstrings, how Python stores them, and how to read them using `help()` — a
skill you will use every time you explore a new library.

### Why you need this

Code without documentation is harder to reuse and share.  When you call
`help(some_function)`, Python is displaying that function's docstring.
Writing your own docstrings is the same skill in reverse: you are the author
providing the documentation that future readers (including yourself) will rely
on.

---

## Do

### Step 1 — Your first docstring

A docstring is a string literal (usually using triple quotes) placed on the
first line of a function body:

```python
def hypotenuse(a, b):
    """Return the length of the hypotenuse given the two shorter sides."""
    import math
    return math.sqrt(a**2 + b**2)
```

The triple-quoted string is not assigned to a variable — Python automatically
stores it as the function's `__doc__` attribute.

---

### Step 2 — Reading a docstring

```python
print(hypotenuse.__doc__)
# Return the length of the hypotenuse given the two shorter sides.

help(hypotenuse)
# Help on function hypotenuse in module __main__:
#
# hypotenuse(a, b)
#     Return the length of the hypotenuse given the two shorter sides.
```

`help()` is the built-in function you will use throughout this course to look
up what any function does — whether it is a function you wrote or one from a
library. You should focus on typing it for the next few lessons. However; its contents will also be available when you type a function using visual studio code.

---

### Step 3 — Multi-line docstrings

Longer functions benefit from a multi-line docstring.  The first line is a
brief summary; a blank line follows; then a fuller description:

```python
def percent_grade(score, total):
    """Return the percentage for a numeric score out of 100.


    Parameters
    ----------
    total: int or float
        The numeric total of marks available on a paper.
    score: int or float
        The numeric score to convert (expected range 0-total).


    Returns
    -------
    float:
        A percentage of the total 75.0.
    """
    percent = score / total
    percent *= 100
    return percent
```

> **Style note:** The "Parameters / Returns" layout above follows the
> [NumPy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html),
> which is widely used in scientific Python.  The
> [Google style](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
> is another common alternative.  Either is fine — consistency matters more
> than which style you choose.

- Write a print statement to calculate a percentage of 76/80. As you write the function, observe the behaviour of  visual studio code, trying to help you.
- Explain what the line `percent *= 100` does.

---

### Step 4 — Module-level docstrings

A docstring at the very top of a `.py` file documents the whole module:

```python
"""Grade calculation utilities for maths mark schemes.

This module provides functions for converting numeric scores to
percentages, letter grades and computing class statistics.
"""

def letter_grade(percentage):
    pass
```



---

### Step 5 — Why docstrings matter for libraries

Every function in Python's standard library has a docstring.  When you type:

```python
import math
help(math.sqrt)
```

Python is printing `math.sqrt.__doc__`.  In the next lesson you will use this
extensively to explore the `math` module.  Writing docstrings for your own
code gives it the same discoverability.

### Step 6 - File layout

A python script file should follow a certain format that makes it easy to follow for all readers.

> import statements
> classes (don't worry about this yet)
> functions
> statements

Organise this file and your future files in this order.

---

## Explore

1. Add docstrings to the `hypotenuse`, `shorter_side`, and `is_right_triangle`
   functions you wrote in Lesson 3.  Run `help()` on each.
2. What happens if you call `help()` on a function that has no docstring?
3. Look up the docstring for `print` by running `help(print)`.  What does the
   `sep` parameter do?
4. Python's [`pydoc`](https://docs.python.org/3/library/pydoc.html) tool can
   generate HTML documentation from docstrings.  Run `python -m pydoc -w grade`
   (assuming your module is called `grade.py`) and open the resulting HTML file.
5. Research the difference between a *docstring* and a *comment* (`#`).  When
   would you use each?

---

[← Lesson 3]({{ site.baseurl }}/lessons/03-mathematics/)
[Next Lesson: Strings →]({{ site.baseurl }}/lessons/06-strings/)
