# Lesson 7 - Lists
# Run this script with:  python3 lists.py


# --- Functions ---
def average(numbers):
    return sum(numbers) / len(numbers)

def highest(numbers):
    return max(numbers)

def lowest(numbers):
    return min(numbers)


# --- Statements ---
# Creating lists
movies = ["The Godfather", "Pulp Fiction", "The Dark Knight", "Forrest Gump", "Inception"]

# Accessing elements
print("Length:", len(movies))
print("First:", movies[0])
print("Last:", movies[-1])
print("Middle:", movies[len(movies)//2])

# Modifying a list
movies.append("The Matrix")
print("After append:", movies)

movies.insert(0, "Star Wars")
print("After insert:", movies)

movies.remove("Forrest Gump")
print("After remove:", movies)

last = movies.pop()
print("After pop:", movies)
print("Removed:", last)

# Useful operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sorted:", sorted(numbers))

numbers.sort()
print("sorted in place:", numbers)
print("sorted() returns a new list, sort() modifies in place")

# for ... in loop
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# Iterating over scores
class_scores = [85, 92, 78, 65, 90]
total = 0
for score in class_scores:
    total += score
average = total / len(class_scores)
print(f"Average score: {average:.1f}")
print(f"Highest score: {max(class_scores)}")
print(f"Lowest score: {min(class_scores)}")

# Functions using lists
data = [72, 85, 91, 68, 77, 88, 95, 60]
print(f"Average: {average(data):.1f}")
print(f"Highest: {highest(data)}")
print(f"Lowest:  {lowest(data)}")

# Building a list with a loop
cubes = []
for n in range(1, 6):
    cubes.append(n ** 3)
print("Cubes:", cubes)

# List comprehension
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]
print("Even cubes:", even_cubes)
