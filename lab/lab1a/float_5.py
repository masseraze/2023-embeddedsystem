import matplotlib.pyplot as plt
# Data for 5 times
bin_counts_5 = [5, 0, 0, 0, 0, 13, 0, 0, 4768, 4487, 3, 0, 0, 106, 614, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Adjust the bins_5_corrected data to match the length of bin_counts_5
bins_5_corrected = [2513 + i*61 for i in range(100)]
bins_5_corrected = bins_5_corrected[:len(bin_counts_5)]

# Plotting the histogram for 5 times data
plt.figure(figsize=(10, 6))
bars = plt.bar(bins_5_corrected, bin_counts_5, align='edge', width=61*0.9, edgecolor="k", alpha=0.7)

# Annotating each bar with its value
for bar in bars:
    yval = bar.get_height()
    if yval != 0:  # Only annotate bars that have a value
        plt.text(bar.get_x() + bar.get_width()/2, yval + 50, str(yval), ha='center', va='bottom')

# Automatically tuning the x-axis for clarity
plt.xticks([i for i in range(2500, 9000, 650)])
plt.xlabel("Number of Cycles")
plt.ylabel("Frequency")
plt.title("Data addition with floating point 5 times $10^4$ trials")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Adding the top and right borders
plt.gca().spines['top'].set_visible(True)
plt.gca().spines['right'].set_visible(True)

plt.show()
