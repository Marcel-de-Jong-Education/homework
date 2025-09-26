# 1. Create a nested list named 'grades' where each inner list represents a student.
#    Each student should have grades for Math, Science, and English.
grades = [
    [85, 90, 88],  # Student 1's grades: Math, Science, English
    [78, 82, 85],  # Student 2's grades: Math, Science, English
    [92, 89, 91]   # Student 3's grades: Math, Science, English
]

# 2. Print the grades of the second student.
# Access the second student (index 1), then print their grades.
print(grades[1])

# 3. Change the Math grade of the first student.
# Modify the first grade in the first student's list.
grades[0][0] = 100

# 4. Add a new student with grades.
# Add a new list to the 'grades' list to represent a new student's grades.
grades.append([95,92,98])

# 5. Print the updated list.
print(grades)
