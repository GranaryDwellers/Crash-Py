# Lesson 9 - Decisions
# Run this script with: python3 decisions.py

score = 75
if score >= 50:
    print("Pass")

score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")


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
    return "U"


for result in [95, 85, 72, 62, 55, 40]:
    print(f"{result} → {grade(result)}")

attendance = 82
completed_homework = True
is_ready_for_trip = attendance >= 80 and completed_homework

if is_ready_for_trip:
    print("Trip form can be issued")
else:
    print("Follow up before issuing the trip form")

mark = 73
if 70 <= mark < 80:
    print("Grade B")


def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"


print(classify_triangle(5, 5, 5))
print(classify_triangle(5, 5, 8))
print(classify_triangle(3, 4, 5))
