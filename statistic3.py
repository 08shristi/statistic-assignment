import random

# Number of simulations
num_rolls = 10000

# Counter for number of times the sum is 7
count_sum_7 = 0

# Simulate rolling two dice 10,000 times
for _ in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    if total == 7:
        count_sum_7 += 1

# Estimated probability
estimated_prob = count_sum_7 / num_rolls

# Theoretical probability
# There are 6 possible ways to get sum = 7 (1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
# Total possible outcomes = 36
theoretical_prob = 6 / 36

# Display results
print("Number of simulations:", num_rolls)
print("Number of times sum = 7:", count_sum_7)
print("Estimated Probability =", round(estimated_prob, 4))
print("Theoretical Probability =", round(theoretical_prob, 4))
print("Difference =", round(abs(estimated_prob - theoretical_prob), 4))
