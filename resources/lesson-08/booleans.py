# Lesson 8 - Booleans and Logic
# Run this script with: python3 booleans.py

is_weekday = True
has_finished_marking = False

print(type(is_weekday))
print(is_weekday)
print(has_finished_marking)

print(5 == 5)
print(5 != 3)
print(9 > 12)
print(9 >= 9)
print(2 < 7)
print(2 <= 2)

passed_exam = True
completed_coursework = False

print(not passed_exam)
print(passed_exam and completed_coursework)
print(passed_exam or completed_coursework)
print(passed_exam != completed_coursework)  # xor
print(not (passed_exam and completed_coursework))  # nand
print(not (passed_exam or completed_coursework))   # nor

score = 73
attendance = 92

print(score >= 50 and attendance >= 90)
print(score < 50 or attendance < 75)
print((score >= 70) != (attendance >= 95))
