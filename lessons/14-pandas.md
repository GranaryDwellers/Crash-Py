---
layout: page
title: "Lesson 14: Pandas"
permalink: /lessons/14-pandas/
---

## Introduction

**What this lesson is about**

`pandas` is Python's premier data analysis library.  Its central object — the
*DataFrame* — is like a spreadsheet inside Python: rows and columns of data
that you can filter, sort, group, and summarise with concise commands.  This
lesson covers loading data from a CSV file, computing descriptive statistics,
and answering real questions about a dataset.

**Why you need this**

Pandas lets you analyse datasets that would be tedious or error-prone to process
manually in Excel.  It forms the backbone of data science in Python and combines
naturally with matplotlib (Lesson 15) for visualisation.

---

## Do

### Step 1 — Install pandas

```bash
pip3 install pandas
```

---

### Step 2 — The dataset

This lesson continues with the student scores dataset.

> **Download:** [student_scores.csv]({{ site.baseurl }}/resources/lesson-09a/student_scores.csv)

---

### Step 3 — Loading a CSV into a DataFrame

```python
import pandas as pd

df = pd.read_csv("student_scores.csv")
print(df.head())         # first 5 rows
print(df.shape)          # (rows, columns)
print(df.columns)        # column names
print(df.dtypes)         # data types of each column
```

---

### Step 4 — Descriptive statistics

```python
print(df.describe())     # count, mean, std, min, 25%, 50%, 75%, max

print(df["Score"].mean())
print(df["Score"].median())
print(df["Score"].std())
print(df["Score"].min())
print(df["Score"].max())
```

---

### Step 5 — Accessing columns and rows

```python
# A single column (returns a Series)
scores = df["Score"]

# Multiple columns (returns a DataFrame)
subset = df[["Name", "Score"]]

# Filter rows where score >= 80
high_scorers = df[df["Score"] >= 80]
print(high_scorers)
```

---

### Step 6 — Grouping data

```python
# Average score per topic
topic_avg = df.groupby("Topic")["Score"].mean()
print(topic_avg)

# Count of each grade
grade_counts = df["Grade"].value_counts()
print(grade_counts)
```

---

### Step 7 — Sorting

```python
# Sort by score descending
sorted_df = df.sort_values("Score", ascending=False)
print(sorted_df.head(10))
```

---

### Step 8 — Adding a new column

```python
def assign_pass_fail(score):
    return "Pass" if score >= 50 else "Fail"

df["Result"] = df["Score"].apply(assign_pass_fail)
print(df[["Name", "Score", "Result"]].head())
```

---

### Step 9 — Saving results to a new CSV

```python
df.to_csv("student_scores_with_results.csv", index=False)
print("Saved.")
```

---

### Step 10 — Reading from Excel

`pandas` can read Excel files directly (requires `openpyxl`):

```python
df_excel = pd.read_excel("student_scores.xlsx")
print(df_excel.head())
```

> **Download:** [pandas_stats.py]({{ site.baseurl }}/resources/lesson-14/pandas_stats.py)

---

## Explore

1. Find the student with the highest score in each topic.  Hint: use
   `groupby` and `idxmax()`.
2. How many students scored below the class average?  Write one line of pandas
   code to answer this.
3. Use `df.pivot_table()` to create a table showing the average score for each
   grade within each topic.
4. The UK Department for Education publishes GCSE results data at
   [explore-education-statistics.service.gov.uk](https://explore-education-statistics.service.gov.uk).
   Download a CSV, load it with pandas, and compute the national average for
   maths.
5. What is the difference between `df.mean()` and `df["Score"].mean()`?

---

[← Lesson 13]({{ site.baseurl }}/lessons/13-requests/)
[Next Lesson: Pandas Graphs →]({{ site.baseurl }}/lessons/15-pandas-graphs/)
