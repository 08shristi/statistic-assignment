# Program to compute the Range, Variance, and Standard Deviation
# using mathematical formulas and display intermediate steps

import math

# Step 1: Take input from the user
data_input = input("Enter numbers separated by space or comma: ")

# Step 2: Convert input string to a list of numbers
data_input = data_input.replace(",", " ")
data = [float(x) for x in data_input.split()]

# Step 3: Calculate required values
n = len(data)
data_min = min(data)
data_max = max(data)
data_range = data_max - data_min
mean = sum(data) / n

# Step 4: Show intermediate steps
print("\n--- Intermediate Steps ---")
print(f"Data: {data}")
print(f"Number of elements (n): {n}")
print(f"Minimum value: {data_min}")
print(f"Maximum value: {data_max}")
print(f"Range = {data_max} - {data_min} = {data_range}")
print(f"Mean = (Sum of all values) / n = {mean}")

# Step 5: Calculate deviations and squared deviations
print("\nValue\tDeviation (x - mean)\tSquared Deviation (x - mean)^2")
squared_diffs = []
for x in data:
    deviation = x - mean
    squared = deviation ** 2
    squared_diffs.append(squared)
    print(f"{x}\t{deviation:.2f}\t\t\t{squared:.2f}")

# Step 6: Calculate variance and standard deviation
sum_squared = sum(squared_diffs)
variance_population = sum_squared / n
stddev_population = math.sqrt(variance_population)

# For sample variance (divide by n-1)
variance_sample = sum_squared / (n - 1) if n > 1 else 0
stddev_sample = math.sqrt(variance_sample) if n > 1 else 0

# Step 7: Display results
print("\n--- Final Results ---")
print(f"Sum of squared deviations = {sum_squared:.2f}")
print(f"Population Variance = {variance_population:.4f}")
print(f"Population Standard Deviation = {stddev_population:.4f}")
print(f"Sample Variance = {variance_sample:.4f}")
print(f"Sample Standard Deviation = {stddev_sample:.4f}")
