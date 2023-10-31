import numpy as np
import matplotlib.pyplot as plt

# Function to calculate metrics
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

# Function to plot CDF
def plot_cdf(cycle, count, label, color='blue'):
    # Calculate the cumulative sum of probabilities to get the CDF
    probability = count / np.sum(count)
    cdf = np.cumsum(probability)

    # Extend the x-axis values
    extended_cycle = np.arange(0, 41)
    # Extend the CDF values to cover the new range
    extended_cdf = np.concatenate([cdf, [1] * (41 - len(cdf))])

    # Plotting the CDF
    plt.plot(extended_cycle, extended_cdf, '-o', label=label, color=color, markersize=5)

    # Annotating points
    #for i, (x, y) in enumerate(zip(extended_cycle, extended_cdf)):
    #    if 5 <= i <= min(9, len(cdf)-1):  # Annotate till the length of actual data
    #        plt.annotate(f'({cycle[i]},{y:.2f})', (x, y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# Function to compute and print metrics
def compute_and_print_metrics(cycle, count, interrupt_number):
    sd, se, mean_cycle, ci_value, ci_lower, ci_upper = calculate_metrics(cycle, count)
    print(f"Interrupt {interrupt_number}:")
    print(f"sd: {sd:.10f} se: {se:.10f} 95% confidence Interval: {mean_cycle:.10f} ± {ci_value:.10f} ci_lower: {ci_lower:.10f} ci_upper: {ci_upper:.10f}")

# Data and calculations for Interrupt 0
cycle = np.arange(0, 40)
count_0 = np.array([0,0,0,90418,25714,31641,2297,2935,3656,2141,2703,304,393,488,295,399,48,55,67,34,63,9,4,10,9,5,0,0,3,0,1,0,0,0,1,0,0,0,0,1
])
compute_and_print_metrics(cycle, count_0, 0)
plot_cdf(cycle, count_0, 'Interrupt 0', color='blue')

# Data and calculations for Interrupt 1
cycle = np.arange(0, 10)
count_1 = np.array([0,0,0,0,0,16240,5478,5805,804,888])
compute_and_print_metrics(cycle, count_1, 1)
plot_cdf(cycle, count_1, 'Interrupt 1', color='green')

# Final adjustments for the combined plot
plt.xlabel('Cycle')
plt.ylabel('Cumulative Probability')
plt.title('CDF for Interrupts 0 and 1(b)')
plt.xticks(np.arange(0, 41, 5))
plt.ylim(0, 1.1)
plt.grid(True)
plt.legend(loc='lower right')
plt.show()