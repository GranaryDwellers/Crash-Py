---
layout: page
title: "Lesson 9: Decisions"
permalink: /lessons/09-decisions/
---

## Introduction

### What this lesson is about

Now that you know how boolean expressions work, this lesson shows you how to
**use** them to control the flow of a program with `if`, `elif`, and `else`.

### Why you need this

A useful program rarely does the same thing every time.  It reacts to scores,
text, file contents, user choices, or calculations.  Decision statements let
Python choose the right action for the situation.

---

## Do

### Step 1 — A basic `if` statement

```python
score = 75

if score >= 50:
    print("Pass")
```

The indented block runs only when the condition is `True`.

---

### Step 2 — `if … else`

```python
score = 45

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

`else` gives the alternative action when the condition is `False`.

---

### Step 3 — `if … elif … else`

```python
def grade(score):
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

print(grade(95))   # A*
print(grade(72))   # B
print(grade(40))   # U
```

Python checks the conditions from top to bottom and uses the first one that is
`True`.

---

### Step 4 — Using a boolean you computed earlier

```python
attendance = 82
completed_homework = True
is_ready_for_trip = attendance >= 80 and completed_homework

if is_ready_for_trip:
    print("Trip form can be issued")
else:
    print("Follow up before issuing the trip form")
```

This is why the previous lesson mattered: an `if` statement needs a boolean
condition to test.

---

### Step 5 — Chaining comparisons

Python allows you to chain comparisons naturally:

```python
mark = 73

if 70 <= mark < 80:
    print("Grade B")
```

---

### Step 6 — Practical example: classifying triangles

```python
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(classify_triangle(5, 5, 5))
print(classify_triangle(5, 5, 8))
print(classify_triangle(3, 4, 5))
```

> **Download:** [decisions.py]({{ site.baseurl }}/resources/lesson-09/decisions.py)

---

## Explore

1. Extend the `grade()` function to also print a short comment alongside the
   grade, e.g. `"A* — Outstanding"`.
2. Write a function `is_valid_triangle(a, b, c)` that returns `True` if the
   three lengths can form a triangle.  (Hint: the sum of any two sides must be
   greater than the third side.)
3. Write a function `fizzbuzz(n)` that returns `"Fizz"` if `n` is divisible by
   3, `"Buzz"` if divisible by 5, `"FizzBuzz"` if divisible by both, and the
   number itself otherwise.
4. What happens if you put the `elif score >= 80` line **before**
   `elif score >= 90` in `grade()`?  Why?
5. Can you write a `grade()` function using a dictionary instead of
   `if … elif`?  (Hint: this is tricky — come back to it after Lesson 11.)

---

[← Lesson 8]({{ site.baseurl }}/lessons/08-booleans/)
[Next Lesson: For Loops with Range →]({{ site.baseurl }}/lessons/10-for-loops/)
