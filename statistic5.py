# Hypothesis Testing: Two-Sample t-test for difference in means

import numpy as np
from scipy import stats

# Step 1: Assume sample data (marks of students in two classes)
class_A = [78, 85, 80, 90, 76, 83, 89, 84, 82, 88]
class_B = [72, 75, 70, 68, 74, 71, 69, 73, 77, 70]

# Step 2: State the hypotheses
print("Null Hypothesis (H0): There is no significant difference between the average marks of Class A and Class B.")
print("Alternative Hypothesis (H1): There is a significant difference between the average marks of Class A and Class B.\n")

# Step 3: Compute sample means
mean_A = np.mean(class_A)
mean_B = np.mean(class_B)
print(f"Mean of Class A = {mean_A:.2f}")
print(f"Mean of Class B = {mean_B:.2f}\n")

# Step 4: Perform two-sample t-test (assuming equal variances)
t_statistic, p_value = stats.ttest_ind(class_A, class_B)

# Step 5: Display the results
print(f"Test Statistic (t) = {t_statistic:.4f}")
print(f"P-value = {p_value:.4f}\n")

# Step 6: Interpret the result (at 5% significance level)
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the Null Hypothesis (H0).")
    print("→ There is a significant difference between the average marks of the two classes.")
else:
    print("Conclusion: Fail to Reject the Null Hypothesis (H0).")
    print("→ There is no significant difference between the average marks of the two classes.")
