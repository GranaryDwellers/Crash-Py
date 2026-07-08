---
layout: page
title: "Lesson 8: Booleans and Logic"
permalink: /lessons/08-booleans/
---

## Introduction

### What this lesson is about

This lesson introduces **booleans** — values that are either `True` or `False`.
You will learn how comparisons such as `==` and `>=` produce booleans, how
logical operators combine them, and how **truth tables** help you reason about
what a boolean expression will do.

### Why you need this

Before a program can make a decision, it needs a condition to test.  Booleans
are those conditions.  They let you ask questions such as *"Is this score at
least 50?"* or *"Is the student present and on time?"*  In the next lesson you
will use these booleans inside `if` statements.

---

## Do

### Step 1 — Meet the `bool` type

Python has a built-in type called `bool` with exactly two values: `True` and
`False`.

```python
is_weekday = True
has_finished_marking = False

print(type(is_weekday))  # <class 'bool'>
print(is_weekday)        # True
print(has_finished_marking)  # False
```

---

### Step 2 — Comparisons produce booleans

These operators compare two values and return either `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | equal to | `5 == 5` |
| `!=` | not equal to | `5 != 3` |
| `>` | greater than | `9 > 4` |
| `>=` | greater than or equal to | `9 >= 9` |
| `<` | less than | `2 < 7` |
| `<=` | less than or equal to | `2 <= 2` |

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(9 > 12)   # False
print(7 <= 7)   # True
```

> **Common mistake:** `=` assigns a value, but `==` compares two values.

---

### Step 3 — What a truth table is

A **truth table** lists every possible input and shows the boolean result for
each one.  It is a compact way to check what an operator does before you use it
inside a larger expression.

For a single boolean such as `a`, there are only two possible inputs: `True`
and `False`.  For two booleans such as `a` and `b`, there are four possible
combinations.

---

### Step 4 — `not` flips a boolean

`not` takes one boolean and reverses it.

| `a` | `not a` |
|---|---|
| `True` | `False` |
| `False` | `True` |

```python
is_absent = False
print(not is_absent)  # True
```

---

### Step 5 — `and`, `or`, and `xor`

`and` is only `True` when **both** inputs are `True`.

| `a` | `b` | `a and b` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

`or` is `True` when **at least one** input is `True`.

| `a` | `b` | `a or b` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

`xor` means **exclusive or**: it is `True` when the inputs are different.
Python does not have an `xor` keyword, but with booleans you can write it as
`a != b`.

| `a` | `b` | `a != b` (`xor`) |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `False` |

```python
passed_exam = True
completed_coursework = False

print(passed_exam and completed_coursework)  # False
print(passed_exam or completed_coursework)   # True
print(passed_exam != completed_coursework)   # True
```

---

### Step 6 — `nand` and `nor`

Python does not have built-in `nand` or `nor` keywords, but they are easy to
build from operators you already know.

- `nand` means **not and**: `not (a and b)`
- `nor` means **not or**: `not (a or b)`

| `a` | `b` | `not (a and b)` (`nand`) | `not (a or b)` (`nor`) |
|---|---|---|---|
| `False` | `False` | `True` | `True` |
| `False` | `True` | `True` | `False` |
| `True` | `False` | `True` | `False` |
| `True` | `True` | `False` | `False` |

```python
logged_in = True
is_admin = False

print(not (logged_in and is_admin))  # nand -> True
print(not (logged_in or is_admin))   # nor -> False
```

---

### Step 7 — Combining comparisons

Comparisons and logical operators work together.

```python
score = 73
attendance = 92

print(score >= 50 and attendance >= 90)  # True
print(score < 50 or attendance < 75)     # False
print(score >= 70 != (attendance >= 95)) # True
```

The result of each comparison is a boolean, and then `and`, `or`, `not`, or an
`xor` expression combines them.

---

### Step 8 — A practical example

```python
temperature = 18
is_raining = True

is_warm_enough = temperature >= 15
should_take_coat = is_raining or temperature < 10

print(is_warm_enough)   # True
print(should_take_coat) # True
```

In the next lesson you will use booleans like these inside `if`, `elif`, and
`else` statements.

> **Download:** [booleans.py]({{ site.baseurl }}/resources/lesson-08/booleans.py)

---

## Explore

1. Write three comparisons that each produce `True`, then three that produce
   `False`.
2. Make a truth table for `not (a != b)`.  What familiar test is this equivalent
   to?
3. Write a boolean expression that is `True` only when a score is between 40 and
   59 inclusive.
4. Suppose `has_pen = False` and `has_pencil = True`.  What do `has_pen or
   has_pencil`, `has_pen and has_pencil`, and `has_pen != has_pencil` produce?
5. Research Python's `^` operator on booleans.  How does it compare with using
   `!=` for `xor`?

---

[← Lesson 7]({{ site.baseurl }}/lessons/07-lists/)
[Next Lesson: Decisions →]({{ site.baseurl }}/lessons/09-decisions/)
