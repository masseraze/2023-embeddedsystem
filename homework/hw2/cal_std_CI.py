import numpy as np
# Given data
cycle = np.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34
])
count = np.array([
    0, 0, 0, 63861, 9102, 10070, 1795, 2028, 2206, 842, 899,
    231, 284, 329, 132, 128, 32, 37, 45, 14, 34,
    5, 3, 8, 1, 2, 0, 0, 1, 0, 0,
    0, 0, 0, 1
])

# Calculate the weighted mean
mean_cycle = np.sum(cycle * count) / np.sum(count)

# Calculate the standard deviation
variance = np.sum(count * (cycle - mean_cycle)**2) / np.sum(count)
sd = np.sqrt(variance)

# Calculate the standard error
n = np.sum(count)
se = sd / np.sqrt(n)

# Calculate the 95% confidence interval
z_value = 1.96  # for 95% confidence
ci_lower = mean_cycle - z_value * se
ci_upper = mean_cycle + z_value * se

sd, (ci_lower, ci_upper)
print("sd:", sd, "se", se, "ci_lower:", ci_lower, "ci_upper:", ci_upper)
