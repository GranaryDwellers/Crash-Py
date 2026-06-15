---
layout: page
title: "Lesson 9: Excel Files"
permalink: /lessons/09-excel-files/
---

## Introduction

**What this lesson is about**

Excel spreadsheets (`.xlsx` files) are common in schools for recording marks,
registers, and data.  This lesson shows you how to read an Excel file into
Python, process the data, and write the results to a new Excel file using the
`openpyxl` library.

**Why you need this**

Being able to automate Excel tasks with Python means you can process large
mark books, generate reports, and transform data far more quickly than by hand.
These skills directly support the pandas lessons (14 and 15) where you will do
even more powerful analysis.

---

## Do

### Step 1 — Install `openpyxl`

Open Terminal and run:

```bash
pip3 install openpyxl
```

---

### Step 2 — The sample dataset

This lesson uses a freely available dataset of fictional student maths scores.
A sample file is provided for download below.

> **Download sample data:** [student_scores.xlsx]({{ site.baseurl }}/resources/lesson-09/student_scores.xlsx)

The spreadsheet has these columns:

| Column | Description |
|---|---|
| `StudentID` | Unique identifier |
| `Name` | Student name |
| `Topic` | Maths topic (Algebra, Geometry, Statistics, …) |
| `Score` | Score out of 100 |
| `Grade` | Letter grade |

---

### Step 3 — Reading an Excel file

Create `excel_files.py`:

```python
import openpyxl

wb = openpyxl.load_workbook("student_scores.xlsx")
ws = wb.active   # select the first sheet

# Print the header row
header = [cell.value for cell in ws[1]]
print(header)

# Print each data row
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

---

### Step 4 — Processing the data

```python
import openpyxl

wb = openpyxl.load_workbook("student_scores.xlsx")
ws = wb.active

scores = []
for row in ws.iter_rows(min_row=2, values_only=True):
    student_id, name, topic, score, grade = row
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Class average: {average:.1f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score:  {min(scores)}")
```

---

### Step 5 — Writing an Excel file

```python
import openpyxl

# Create a new workbook
wb_out = openpyxl.Workbook()
ws_out = wb_out.active
ws_out.title = "Summary"

# Write a header
ws_out.append(["Metric", "Value"])

# Write some data
ws_out.append(["Average Score", 76.4])
ws_out.append(["Highest Score", 98])
ws_out.append(["Lowest Score", 42])

wb_out.save("summary.xlsx")
print("summary.xlsx saved.")
```

---

### Step 6 — Copying and transforming data

Read `student_scores.xlsx`, add a "Pass/Fail" column, and save as a new file:

```python
import openpyxl

wb_in = openpyxl.load_workbook("student_scores.xlsx")
ws_in = wb_in.active

wb_out = openpyxl.Workbook()
ws_out = wb_out.active
ws_out.title = "Results"

# Copy header and add new column
header = [cell.value for cell in ws_in[1]]
header.append("Pass/Fail")
ws_out.append(header)

for row in ws_in.iter_rows(min_row=2, values_only=True):
    student_id, name, topic, score, grade = row
    result = "Pass" if score >= 50 else "Fail"
    ws_out.append([student_id, name, topic, score, grade, result])

wb_out.save("results.xlsx")
print("results.xlsx saved.")
```

---

### Step 7 — Basic formatting

```python
from openpyxl.styles import Font, PatternFill

ws_out["A1"].font = Font(bold=True)
ws_out["A1"].fill = PatternFill(fill_type="solid", fgColor="FFFF00")
```

> **Download:** [excel_files.py]({{ site.baseurl }}/resources/lesson-09/excel_files.py)

---

## Explore

1. Modify the script to count how many students achieved each grade (A*, A, B,
   C, D, U) and write the counts to a new sheet called "Grade Distribution".
2. The UK Department for Education publishes open data on exam results at
   [explore-education-statistics.service.gov.uk](https://explore-education-statistics.service.gov.uk).
   Download a dataset, open it in Python, and compute a summary statistic.
3. How would you sort the rows by score before writing them to the output file?
   Hint: read all rows into a list of tuples and use `sorted()`.
4. What happens if a cell contains `None` (an empty cell)?  Write code to
   handle this safely.
5. `openpyxl` can also create charts inside Excel files.  Search the
   [openpyxl documentation](https://openpyxl.readthedocs.io) to find out how.

---

[← Lesson 8]({{ site.baseurl }}/lessons/08-dictionaries/)
[Next Lesson: CSV Files →]({{ site.baseurl }}/lessons/09a-csv-files/)
