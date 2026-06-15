---
layout: page
title: "Lesson 1: Installation & Hello World"
permalink: /lessons/01-installation/
---

## Introduction

**What this lesson is about**

Before writing any Python code you need the right tools on your computer.
This lesson walks you through installing Python, a code editor (Visual Studio
Code), and a package manager (Homebrew) on a Mac.  You will then write your
very first Python program — the traditional "Hello, World!" — and learn how to
run it from a terminal.

**Why you need this**

Every lesson that follows requires Python to be installed and a place to write
code.  Getting comfortable with the terminal is an essential skill: it lets you
run programs, install packages, and automate tasks that would otherwise take many
mouse-clicks.

---

## Do

### Step 1 — Install Homebrew (Mac)

[Homebrew](https://brew.sh) is a package manager for macOS.  It makes
installing and updating developer tools straightforward.

1. Open **Terminal** (search for "Terminal" in Spotlight with `⌘ Space`).
2. Paste the following command and press `Return`:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Follow the on-screen instructions.  You may be asked for your Mac password.
4. Once finished, verify the installation:

```bash
brew --version
```

You should see a version number such as `Homebrew 4.x.x`.

---

### Step 2 — Install Python

Python 3 can now be installed with a single Homebrew command:

```bash
brew install python
```

Verify the installation:

```bash
python3 --version
```

You should see `Python 3.x.x`.

---

### Step 3 — Install Visual Studio Code

```bash
brew install --cask visual-studio-code
```

Open VS Code from your Applications folder (or type `code .` in Terminal once
the shell integration is set up — VS Code will prompt you to do this the first
time it opens).

Install the **Python extension**:

1. Click the Extensions icon in the left sidebar (or press `⌘ Shift X`).
2. Search for **Python** (published by Microsoft).
3. Click **Install**.

---

### Step 4 — Create a project folder

In Terminal:

```bash
mkdir ~/crash-py
cd ~/crash-py
```

---

### Step 5 — Write Hello World

Open VS Code in your new folder:

```bash
code .
```

Create a new file called `hello_world.py` (File → New File, then save as
`hello_world.py`).  Type the following:

```python
print("Hello, World!")
```

Save the file with `⌘ S`.

---

### Step 6 — Run the script (Mac)

In Terminal (make sure you are in the `~/crash-py` folder):

```bash
python3 hello_world.py
```

You should see:

```
Hello, World!
```

---

### Step 7 — Run the script (Windows)

> **Note:** If you are using a Windows machine the steps above are slightly
> different.

1. Download Python from [python.org/downloads](https://www.python.org/downloads/).
   During installation tick **"Add Python to PATH"**.
2. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
3. Open **Command Prompt** (`Windows + R`, type `cmd`, press Enter).
4. Navigate to your project folder:

```cmd
cd %USERPROFILE%\crash-py
```

5. Run the script:

```cmd
python hello_world.py
```

On Windows the command is `python` rather than `python3`.

---

### Step 8 — Extend Hello World

Edit `hello_world.py` to print a few more lines:

```python
print("Hello, World!")
print("I am learning Python.")
print("I am a maths teacher.")
```

Run the script again and watch all three lines appear.

> **Download:** [hello_world.py]({{ site.baseurl }}/resources/lesson-01/hello_world.py)

---

## Explore

1. What happens if you misspell `print` as `Print`?  Try it and read the error
   message carefully — Python's error messages are usually very helpful.
2. Can you print a number instead of text?  Try `print(42)`.
3. What is the difference between `print("Hello")` and `print(Hello)` (without
   quotes)?  Why does one work and the other not?
4. In Terminal, type `python3 --help`.  What information does it give you?
5. The `print` function can take multiple values separated by commas:
   `print("Hello", "World")`.  What does this produce?  How is it different
   from `print("Hello World")`?

---

[← Back to Lessons]({{ site.baseurl }}/lessons/)
[Next Lesson: Functions →]({{ site.baseurl }}/lessons/02-functions/)
