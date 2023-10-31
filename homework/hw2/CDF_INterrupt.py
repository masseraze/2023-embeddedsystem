# This is for Interrrupt 1
import matplotlib.pyplot as plt
import numpy as np
# Calculate the cumulative sum of probabilities to get the CDF
count_new = np.array([0, 0, 0, 0, 0, 20680, 3382, 3634, 831, 890])
probability = count_new / np.sum(count_new)
cdf = np.cumsum(probability)

# Plotting the extended CDF with selected annotations
# Extend the x-axis values
extended_cycle = np.arange(0, 36)
# Extend the CDF values to cover the new range
extended_cdf = np.concatenate([cdf, [1] * (36 - len(cdf))])


plt.figure(figsize=(12, 7))
plt.plot(extended_cycle, extended_cdf, '-o', color='green', markersize=5)

# Annotating points from 5 to 9 with their coordinates
for x, y in zip(extended_cycle, extended_cdf):
    if 5 <= x <= 9:
        plt.annotate(f'({x},{y:.2f})', (x, y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.xlabel('Cycle')
plt.ylabel('Cumulative Probability')
plt.title('CDF for Interrupt 1')
plt.xticks(np.arange(0, 36, 5))
plt.ylim(0, 1.1)
plt.grid(True)

plt.show()
