---
layout: page
title: "Lesson 4: Docstrings and Code Documentation"
permalink: /lessons/04-docstrings/
---

## Introduction

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

We will continue with the `mathematics.py` file you created last lesson in this lesson.

A docstring is a string literal (usually using triple quotes) placed on the
first line of a function body:

Example:

```python
import math          # Always put import statements at the top of a file, do not repeat them

def square(number):
    return (number * number)

def hypotenuse(a, b): # Always put functions after import statements, but before other statements, keep functions together
    """Return the length of the hypotenuse given the two shorter sides."""
    result = square(a)
    result += square(b)
    return math.sqrt(result)
```

The triple-quoted string is not assigned to a variable — Python automatically
stores it as the function's `__doc__` attribute.

1. When you call this function - what effect does the docstring have?
2. What does the `+=` operator do? [hint](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements)

---

### Step 2 — Reading a docstring

Example:

```python
print(hypotenuse.__doc__)

help(hypotenuse)
```

`help()` is the built-in function you will use throughout this course to look
up what any function does — whether it is a function you wrote or one from a
library.

1. Try the example code.
2. When typing the fuction - does visual studio code do anything as you are typing. You will need to keep an eye on the screen as you type.

---

### Step 3 — Multi-line docstrings

Longer functions benefit from a multi-line docstring.  The first line is a
brief summary; a blank line follows; then a fuller description:

Example: (do not type this out, just for reading)

```python
def letter_grade(score):
    """Return the letter grade for a numeric score out of 100.

    Uses the standard UK grading scale:
        A*: 90–100, A: 80–89, B: 70–79, C: 60–69, D: 50–59, U: 0–49.

    Parameters
    ----------
    score : int or float
        The numeric score to convert (expected range 0–100).

    Returns
    -------
    str
        A single letter grade (e.g. "A", "B", "U").
    """
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "U"
```

> **Style note:** The "Parameters / Returns" layout above follows the
> [NumPy docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html),
> which is widely used in scientific Python.  The
> [Google style](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
> is another common alternative.  Either is fine — consistency matters more
> than which style you choose.

1. The example above purposely uses things we haven't learned about yet.  But it should still be readable. Without writing the code out - What do you expect the output to be if the score was:
    1. 89
    2. 90.6
    3. 102
    4. -5
    5. 95.5
    6. "4"
    7. None

2. Research [numpy](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) and [google](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings) conventions for doc strings.  Choose one and only one for the mathematics.py file
3. Add docstrings to all functions in the style chosen.

Through the rest of the course you should add doc strings to each function.

---

### Step 4 — Module-level docstrings

A docstring at the very top of a `.py` file documents the whole module:

Example:
```python
"""Grade calculation utilities for maths mark schemes.

This module provides functions for converting numeric scores to
letter grades and computing class statistics.
"""

import math

def letter_grade(score):
    ...
```

1. Why might these docstrings be useful to a programmer?
2. add a module docstring to the `mathematics.py` file (a file is called a module in python)

Throughout this course module docstrings should be added if a module is to be imported.

---

## Explore

1. What happens if you call `help()` on a function that has no docstring?
2. Look up the docstring for `print` by running `help(print)`.  What does the
   `sep` parameter do?
3. Look up the docstring for `math.sqrt()`. 
4. Python's [`pydoc`](https://docs.python.org/3/library/pydoc.html) tool can
   generate HTML documentation from docstrings.  Run `python -m pydoc -w mathematics` (assuming your file is named `mathematics.py`) and open the resulting HTML file.
5. Research the difference between a *docstring* and a *comment* (`#`).  When
   would you use each?
6. Go back and organise your mathematics file. From this point forward keep your files organised.

---

[← Lesson 3]({{ site.baseurl }}/lessons/03-mathematics/)
[Next Lesson: Strings →]({{ site.baseurl }}/lessons/05-strings/)
