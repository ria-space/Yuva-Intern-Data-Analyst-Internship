"""Descriptive statistics examples using Python's standard library."""
from statistics import mean, median, multimode, variance, stdev

marks = [72, 81, 59, 88, 76, 63, 92, 69]
print("Mean:", mean(marks))
print("Median:", median(marks))
print("Mode(s):", multimode(marks))
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Range:", max(marks) - min(marks))
print("Sample variance:", variance(marks))
print("Sample standard deviation:", stdev(marks))

# Probability example: fair six-sided die
probability_of_even = 3 / 6
print("P(even result):", probability_of_even)
