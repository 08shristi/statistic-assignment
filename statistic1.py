# Program to calculate Mean, Median, Mode, and Weighted Mean

from statistics import mean, median, mode

# Step 1: Take input from the user
data_input = input("Enter the dataset values separated by space or comma: ")

# Step 2: Convert input string to a list of numbers
data_input = data_input.replace(",", " ")
data = [float(x) for x in data_input.split()]

# Step 3: Calculate Mean, Median, and Mode
mean_value = mean(data)
median_value = median(data)

# For mode, handle cases where multiple modes exist
try:
    mode_value = mode(data)
except:
    mode_value = "No unique mode (multiple modes exist)"

# Step 4: Weighted Mean Calculation
print("\n--- Weighted Mean ---")
print("Enter corresponding weights for each data value (same number of values):")
weights_input = input("Enter weights separated by space or comma: ")
weights_input = weights_input.replace(",", " ")
weights = [float(x) for x in weights_input.split()]

if len(weights) != len(data):
    print("Error: The number of weights must match the number of data values.")
else:
    weighted_sum = sum([data[i] * weights[i] for i in range(len(data))])
    total_weight = sum(weights)
    weighted_mean = weighted_sum / total_weight

    # Step 5: Display Results
    print("\n--- Results ---")
    print(f"Data: {data}")
    print(f"Weights: {weights}")
    print(f"Mean = {mean_value:.2f}")
    print(f"Median = {median_value:.2f}")
    print(f"Mode = {mode_value}")
    print(f"Weighted Mean = {weighted_mean:.2f}")
