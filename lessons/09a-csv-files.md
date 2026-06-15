---
layout: page
title: "Lesson 9a: CSV Files"
permalink: /lessons/09a-csv-files/
---

## Introduction

**What this lesson is about**

CSV (*Comma-Separated Values*) is the simplest and most widely supported format
for tabular data.  Almost every application — Excel, Google Sheets, databases —
can export to and import from CSV.  This lesson covers Python's built-in `csv`
module for reading, writing, and transforming CSV files.

**Why you need this**

CSV files are everywhere in education data: registers, mark sheets, assessment
exports.  Because CSV is plain text you can open it in any editor, making it
easier to inspect and debug than a binary Excel file.  Many of the large public
datasets you will encounter in later lessons are provided in CSV format.

---

## Do

### Step 1 — The sample data

This lesson uses the same student scores dataset from Lesson 9, but in CSV format.

> **Download:** [student_scores.csv]({{ site.baseurl }}/resources/lesson-09a/student_scores.csv)

Open it in a text editor to see its structure:

```
StudentID,Name,Topic,Score,Grade
1,Alice,Algebra,85,A
2,Bob,Geometry,72,C
...
```

---

### Step 2 — Reading a CSV file

```python
import csv

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Each `row` is a **list** of strings.

---

### Step 3 — Skipping the header row

```python
import csv

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)   # read (and skip) the first row
    print("Columns:", header)

    for row in reader:
        print(row)
```

---

### Step 4 — DictReader (recommended)

`csv.DictReader` maps each row to a dictionary using the header as keys —
much easier to work with:

```python
import csv

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], "scored", row["Score"])
```

---

### Step 5 — Computing statistics from CSV

```python
import csv

scores = []

with open("student_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        scores.append(int(row["Score"]))

print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest:  {min(scores)}")
```

Note: values from a CSV are always strings — convert them with `int()` or
`float()` as needed.

---

### Step 6 — Writing a CSV file

```python
import csv

results = [
    ["Name", "Score", "Grade"],
    ["Alice", 85, "A"],
    ["Bob",   72, "C"],
    ["Charlie", 95, "A*"],
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

print("output.csv written.")
```

---

### Step 7 — Converting CSV to Excel

```python
import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open("student_scores.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)

wb.save("student_scores_from_csv.xlsx")
print("Excel file created.")
```

> **Download:** [csv_files.py]({{ site.baseurl }}/resources/lesson-09a/csv_files.py)

---

## Explore

1. Extend the statistics script to also print how many students achieved each
   grade.  Use a dictionary to count them.
2. Write a script that reads `student_scores.csv` and writes a new CSV
   containing only the rows where `Score >= 70`.
3. Some CSV files use a semicolon (`;`) as the delimiter instead of a comma.
   How would you tell `csv.reader` to use a different delimiter?  Check the
   documentation for the `delimiter` parameter.
4. What does the `newline=""` argument do in `open()`?  What goes wrong if you
   leave it out on Windows?
5. The UK government publishes thousands of open datasets in CSV format at
   [data.gov.uk](https://data.gov.uk).  Download a dataset that interests you,
   load it with `csv.DictReader`, and print the column names.

---

[← Lesson 9]({{ site.baseurl }}/lessons/09-excel-files/)
[Next Lesson: Markdown →]({{ site.baseurl }}/lessons/10-markdown/)
