# Simple Linear Regression and Correlation Coefficient Calculation

# Sample data: Study hours (x) vs Exam scores (y)
x = [2, 3, 4, 5, 6, 8, 9, 10]   # study hours
y = [40, 50, 60, 65, 70, 80, 85, 95]  # exam scores

# Step 1: Calculate means of x and y
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Step 2: Calculate correlation coefficient (r)
numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
denominator = (sum((x[i] - mean_x)**2 for i in range(len(x))) *
               sum((y[i] - mean_y)**2 for i in range(len(y)))) ** 0.5
r = numerator / denominator

# Step 3: Calculate slope (b) and intercept (a) using least squares method
b = numerator / sum((x[i] - mean_x)**2 for i in range(len(x)))
a = mean_y - b * mean_x

# Step 4: Display the regression equation and correlation
print("Mean of X =", round(mean_x, 2))
print("Mean of Y =", round(mean_y, 2))
print("Correlation coefficient (r) =", round(r, 4))
print(f"Regression line: y = {a:.2f} + {b:.2f}x")

# Step 5: Predict a value (optional example)
study_hours = 7
predicted_score = a + b * study_hours
print(f"Predicted exam score for {study_hours} study hours = {predicted_score:.2f}")
