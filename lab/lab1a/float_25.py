import matplotlib.pyplot as plt

# Data for 25 times
bin_counts_25 = [18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3285, 0, 1696, 3389, 1, 1609, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Correcting the mismatch in lengths of bins_25_corrected and bin_counts_25
bins_25_corrected = [9133 + i*73 for i in range(100)]
bins_25_corrected = bins_25_corrected[:len(bin_counts_25)]

# Plotting the histogram for 25 times data
plt.figure(figsize=(10, 6))
bars = plt.bar(bins_25_corrected, bin_counts_25, align='edge', width=73*0.9, edgecolor="k", alpha=0.7)

# Annotating each bar with its value
for bar in bars:
    yval = bar.get_height()
    if yval != 0:  # Only annotate bars that have a value
        plt.text(bar.get_x() + bar.get_width()/2, yval + 50, str(yval), ha='center', va='bottom')

# Adjusting the x-axis for clarity
plt.xticks([i for i in range(8000, 18000, 1000)])
plt.xlabel("Number of Cycles")
plt.ylabel("Frequency")
plt.title("Data addition with floating point 25 times $10^4$ trials")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
