# Lesson 5 - Strings
# Run this script with:  python3 strings.py


# --- Functions ---
def format_score(name, score):
    return f"{name} scored {score}%"

def process_text(text):
    return text.strip().lower()

def format_csv_line(csv_line):
    parts = csv_line.split(",")
    return " - ".join(parts)

def analyze_string(word):
    return f"First 3: {word[:3]}, Last 3: {word[-3:]}, Length: {len(word)}"

def format_score_grade(score, grade):
    return f"Score: {score}, Grade: {grade}"


# --- Statements ---
# Creating strings
name = "Alice"
subject = 'Mathematics'
note = """This is a
multi-line string."""
print(note)

# Concatenation and repetition
first = "Hello"
second = "World"
message = first + ", " + second + "!"
print(message)

line = "-" * 30
print(line)

# f-strings
score = 87
print(f"{name} scored {score}%")
print(f"{name} scored {score:.1f}%")
print(f"Double her score: {score * 2}")

print(format_score("Bob", 92))
print(format_score("Charlie", 78))

# String methods
text = "  Hello, World!  "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("World", "Python"))
print(text.strip().startswith("Hello"))
print(text.strip().endswith("!"))

print(process_text("  Hello, World!  "))
print(process_text("  PYTHON PROGRAMMING  "))

# Splitting and joining
csv_line = "Alice,87,A"
parts = csv_line.split(",")
print(parts)
rejoined = " | ".join(parts)
print(rejoined)

print(format_csv_line("Alice,87,A"))
print(format_csv_line("Bob,92,B"))
print(format_csv_line("Charlie,78,C"))

# Indexing and slicing
word = "Mathematics"
print(word[0])      # M
print(word[-1])     # s
print(word[0:4])    # Math, start at index 0 and go up to (but not including) index 4
print(word[4:])     # ematics, start at index 4 and go to the end
print(word[:4])     # Math, start at the beginning and go up to (but not including) index 4
print(word[2:8:2])  # tea, start at index 2 and go up to (but not including) index 8, stepping by 2
print(len(word))    # 11

print(analyze_string("Mathematics"))
print(analyze_string("Python"))
print(analyze_string("Programming"))
print(word[2:8])  # "them"

# Checking content
sentence = "The quick brown fox"
print("quick" in sentence)
print(sentence.count("o"))
print(sentence.find("brown"))

# Converting to string
grade = "A*"
print("Score: " + str(score))
print(f"Score: {score}, Grade: {grade}")

print(format_score_grade(87, "A"))
print(format_score_grade(92, "A*"))
print(format_score_grade(78, "B"))
