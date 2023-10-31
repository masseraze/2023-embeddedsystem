import numpy as np

def calculate_metrics(cycle, count):
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
    
    ci_value = z_value * se

    return sd, se, mean_cycle, ci_value, ci_lower, ci_upper

# Define your cycle and count data
cycle_0 = np.arange(0, 35)
count_0 = np.array([
    0, 0, 0, 63861, 9102, 10070, 1795, 2028, 2206, 842, 899,
    231, 284, 329, 132, 128, 32, 37, 45, 14, 34,
    5, 3, 8, 1, 2, 0, 0, 1, 0, 0,
    0, 0, 0, 1
])
cycle_1 = np.arange(0, 10)
count_1 = np.array([0, 0, 0, 0, 0, 20680, 3382, 3634, 831, 890])
# Compute metrics
sd_0, se_0, mean_cycle_0, ci_value_0, ci_lower_0, ci_upper_0 = calculate_metrics(cycle_0, count_0)
sd_1, se_1, mean_cycle_1, ci_value_1, ci_lower_1, ci_upper_1 = calculate_metrics(cycle_1, count_1)
# Print the results
print("Interrupt 0:")
print(f"sd: {sd_0:.10f} se: {se_0:.10f} 95% confidence Interval: {mean_cycle_0:.10f} ± {ci_value_0:.10f} ci_lower: {ci_lower_0:.10f} ci_upper: {ci_upper_0:.10f}")
print("Interrupt 1:")
print(f"sd: {sd_1:.10f} se: {se_1:.10f} 95% confidence Interval: {mean_cycle_1:.10f} ± {ci_value_1:.10f} ci_lower: {ci_lower_1:.10f} ci_upper: {ci_upper_1:.10f}")
