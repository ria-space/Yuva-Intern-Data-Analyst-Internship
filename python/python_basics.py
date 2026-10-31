"""Python fundamentals examples for Assessment 01."""
# Variables and built-in data types
student_age = 19
study_hours = 2.5
student_name = "Student_01"
is_enrolled = True
print(type(student_age), type(study_hours), type(student_name), type(is_enrolled))

# Operators
a, b = 10, 3
print("Addition:", a + b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Conditional statements
marks = 76
if marks >= 75:
    print("Grade category: Distinction")
elif marks >= 60:
    print("Grade category: First class")
elif marks >= 40:
    print("Grade category: Pass")
else:
    print("Grade category: Needs improvement")

# Loops
for number in range(1, 6):
    print("Iteration:", number)

# Function
def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("At least one value is required.")
    return sum(values) / len(values)

sample_marks = [72, 81, 59, 88]
print("Average:", calculate_average(sample_marks))

# Collections
subjects = ["Python", "Statistics", "SQL"]       # list
coordinates = (19.0, 72.8)                       # tuple
unique_scores = {72, 81, 59, 72}                 # set
student = {"name": "Student_01", "marks": 72}    # dictionary
print(subjects, coordinates, unique_scores, student)

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
