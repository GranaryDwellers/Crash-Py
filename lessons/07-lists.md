---
layout: page
title: "Lesson 7: Lists"
permalink: /lessons/07-lists/
---

## Introduction

### What this lesson is about

A *list* is an ordered, changeable collection of items.  Items in a list can be
numbers, strings, or even other lists.  This lesson covers creating lists,
accessing their elements, modifying them, and using the powerful `for … in`
loop to process each item in turn.

### Why you need this

Virtually every real-world dataset is a collection of items — student names,
test scores, exam results.  Lists are the primary way Python stores and
processes collections, and the `for … in` loop is the standard way to work
through them.

---

## Do

### Step 1 — Creating a list

```python
scores = [85, 92, 78, 65, 90]
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
mixed = [1, "hello", 3.14, True]   # Lists can mix types
empty = []
```

1) Create a new file named `lists.py` for this lesson
2) Create a list of your 5 favorite movie titles as strings, assigned to a variable named `movies`


---

### Step 2 — Accessing elements

Lists are *zero-indexed* sequences — the first element is at index `0`:

```python
print(scores[0])    # 85  — first element
print(scores[-1])   # 90  — last element
print(scores[1:3])  # [92, 78]  — slice (up to but not including index 3)
print(len(scores))  # 5  — number of elements
```
This is the same concept as strings, but now we're working with sequences of items instead of individual characters.

1) Print the length of your movie list
2) Print the first and last movie titles in your list
3) Print the middle movie title(s) in your list

---

### Step 3 — Modifying a list

```python
scores[2] = 80          # Change the third element
scores.append(95)       # Add to the end
scores.insert(0, 70)    # Insert at position 0
scores.remove(65)       # Remove the first occurrence of 65
last = scores.pop()     # Remove and return the last element
print(scores)
```

1) Add a new movie to the end of your list, print the updated list
2) Add a new movie to the beginning of your list, print the updated list
3) Remove a movie from your list, print the updated list
4) Remove the last movie from your list, print the updated list

---

### Step 4 — Useful list operations

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(sum(numbers))       # 31
print(min(numbers))       # 1
print(max(numbers))       # 9
print(sorted(numbers))    # [1, 1, 2, 3, 4, 5, 6, 9]  — returns new sorted list
numbers.sort()            # sorts in place (modifies the original)
print(numbers)
```
1) Print the sum of the numbers
2) Print the minimum and maximum values
3) Print the sorted list
4) Sort the list in place and print it
5) Explain what `sorted()` does vs `sort()`
---

### Step 5 — `for … in` loop

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print("Hello,", name)
```

The loop variable (`name`) takes the value of each element in turn.

1) Create a loop that prints each movie title in your list
2) Create a loop that prints each movie title in your list with an index number prefix (e.g., "1. Movie Title")

---

### Step 6 — Iterating over scores

```python
scores = [85, 92, 78, 65, 90]
total = 0

for score in scores:
    total = total + score

average = total / len(scores)
print(f"Average score: {average:.1f}")
```
1) Calculate and print the average score
2) Find and print the highest score
3) Find and print the lowest score
---

### Step 7 — Combining lists and functions

```python
def average(numbers):
    return sum(numbers) / len(numbers)

def highest(numbers):
    return max(numbers)

class_scores = [72, 85, 91, 68, 77, 88, 95, 60]

```
1) Calculate and print the average score of `class_scores`
2) Find and print the highest score in `class_scores`
3) Find and print the lowest score in `class_scores`
---

### Step 8 — Building a list with a loop

```python
# Squares of 1 to 10
squares = []
for n in range(1, 11):
    squares.append(n ** 2)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

1) Create a list of the cubes of numbers 1 to 5 using a loop


---

### Step 9 — List comprehension (bonus)

Python has a compact syntax for building lists called a *list comprehension*:

```python
squares = [n ** 2 for n in range(1, 11)]
print(squares)
```

This is equivalent to the loop above but shorter.

1) Create a list of the cubes of even numbers from 1 to 10 using a list comprehension

> **Download:** [lists.py]({{ site.baseurl }}/resources/lesson-07/lists.py)

---

## Explore

1. Write a function `above_average(scores)` that returns a new list containing
   only the scores that are above the average.
2. What happens when you try to access `scores[10]` on a list with only 5
   elements?  What is this error called?
3. Lists can contain other lists (nested lists).  Create a list of three
   students, where each student is themselves a list of `[name, score]`.
   Write code to print the name and score of each student.
4. The `in` keyword works with lists: `85 in scores`.  How would you use this
   to check if a particular score appears in the list?
5. Research the difference between `.sort()` and `sorted()`.  When would you
   prefer one over the other?

---

[← Lesson 6]({{ site.baseurl }}/lessons/06-text-files/)
[Next Lesson: Booleans and Logic →]({{ site.baseurl }}/lessons/08-booleans/)
