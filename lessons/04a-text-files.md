---
layout: page
title: "Lesson 4a: Text Files"
permalink: /lessons/04a-text-files/
---

## Introduction

**What this lesson is about**

Programs frequently need to read data from files and write results back to files.
This lesson introduces Python's built-in file operations: opening a file,
reading its contents, writing new content, and the `with` statement that ensures
files are closed safely.

**Why you need this**

Most real-world data lives in files: student registers, mark sheets, resources
for lessons.  Being able to read from and write to text files gives your Python
programs a way to persist information between runs and process data in bulk.

---

## Do

### Step 1 — Writing to a file

```python
with open("notes.txt", "w") as f:
    f.write("Line one\n")
    f.write("Line two\n")
    f.write("Line three\n")

print("File written.")
```

- `"w"` means *write* mode — it creates the file if it does not exist, or
  **overwrites** it if it does.
- The `with` statement automatically closes the file when the block ends, even
  if an error occurs.
- `\n` is a newline character.

---

### Step 2 — Reading an entire file

```python
with open("notes.txt", "r") as f:
    contents = f.read()

print(contents)
```

`"r"` means *read* mode (the default, so you can omit it).

---

### Step 3 — Reading line by line

```python
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the trailing newline
```

This approach is memory-efficient for large files because it reads one line at
a time.

---

### Step 4 — Reading all lines into a list

```python
with open("notes.txt", "r") as f:
    lines = f.readlines()

print(lines)          # ['Line one\n', 'Line two\n', 'Line three\n']
print(len(lines))     # 3
print(lines[0].strip())  # Line one
```

---

### Step 5 — Appending to a file

```python
with open("notes.txt", "a") as f:   # "a" = append mode
    f.write("Line four\n")
```

`"a"` adds content to the *end* of the file without erasing what is already
there.

---

### Step 6 — A practical example: saving a times table

```python
def save_times_table(n, filename):
    with open(filename, "w") as f:
        for i in range(1, 13):
            line = f"{i} × {n} = {i * n}\n"
            f.write(line)

save_times_table(7, "seven_times_table.txt")
print("Times table saved.")
```

---

### Step 7 — Handling a missing file safely

```python
try:
    with open("missing_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("The file does not exist.")
```

The `try … except` pattern catches errors and lets your program respond
gracefully rather than crashing.

---

### Sample file

> **Download:** [sample.txt]({{ site.baseurl }}/resources/lesson-04a/sample.txt)
> — a plain-text file containing a short poem, for practice.

> **Download:** [text_files.py]({{ site.baseurl }}/resources/lesson-04a/text_files.py)

---

## Explore

1. Write a program that reads `sample.txt` and counts how many lines are in it.
2. Write a program that reads `sample.txt` and prints only lines that contain
   the word "the" (case-insensitive).
3. Write a function `word_count(filename)` that returns the number of words
   in a text file.  Hint: split each line on spaces.
4. What happens if you open a file in `"w"` mode that already has content?
   Write an experiment to find out.
5. Write a program that takes a list of student names and scores and saves them
   to a file with one entry per line, e.g. `"Alice: 87"`.  Then write a second
   program that reads that file back and prints the name of the highest scorer.

---

[← Lesson 4]({{ site.baseurl }}/lessons/04-strings/)
[Next Lesson: Lists →]({{ site.baseurl }}/lessons/05-lists/)
