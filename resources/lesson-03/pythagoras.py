# Lesson 3 - Mathematical Operations & Pythagoras
# Run this script with:  python3 pythagoras.py

import math


# --- Number types ---
a = 10        # int
b = 3.5       # float
print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>

# --- Arithmetic operators ---
print(5 + 3)    # 8
print(10 - 4)   # 6
print(3 * 7)    # 21
print(15 / 4)   # 3.75
print(15 // 4)  # 3
print(15 % 4)   # 3
print(2 ** 8)   # 256

# --- The math module ---
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(math.floor(3.9))  # 3
print(math.ceil(3.1))   # 4

# --- Pythagoras: hypotenuse ---
def hypotenuse(a, b):
    """Return the length of the hypotenuse given the two shorter sides."""
    return math.sqrt(a**2 + b**2)


print(hypotenuse(3, 4))    # 5.0
print(hypotenuse(5, 12))   # 13.0


# --- Pythagoras: shorter side ---
def shorter_side(hyp, a):
    """Return the missing shorter side given the hypotenuse and one side."""
    if a >= hyp:
        raise ValueError(f"Side {a} cannot be >= hypotenuse {hyp}")
    return math.sqrt(hyp**2 - a**2)


print(shorter_side(5, 3))    # 4.0
print(shorter_side(13, 5))   # 12.0


# --- Named arguments and formatting ---
c = hypotenuse(a=3, b=4)
print(f"Hypotenuse: {c:.4f}")

b_side = shorter_side(hyp=13, a=5)
print(f"Short side: {round(b_side, 2)}")


# --- Order of operations ---
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20


# --- Triangle classifier ---
def classify_triangle(a, b, c):
    """Classify a triangle by its side lengths."""
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


print(classify_triangle(5, 5, 5))  # Equilateral
print(classify_triangle(5, 5, 8))  # Isosceles
print(classify_triangle(3, 4, 5))  # Scalene
