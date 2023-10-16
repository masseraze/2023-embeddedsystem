import matplotlib.pyplot as plt
# New data for data addition with integers 5 times
min_value_data_addition = 63
max_value_data_addition = 740
bin_size_data_addition = 6
bin_counts_data_addition = [
    9012, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 987, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1
]

# Calculate bin labels for the new data
bin_labels_data_addition = [min_value_data_addition + i * bin_size_data_addition for i in range(len(bin_counts_data_addition))]

# Plotting the histogram with the requested adjustments
plt.figure(figsize=(10, 6))
bars_data_addition = plt.bar(range(len(bin_counts_data_addition)), bin_counts_data_addition, align='edge', width=0.9, edgecolor="k", alpha=0.7)

# Adding the top and right borders
plt.gca().spines['top'].set_visible(True)
plt.gca().spines['right'].set_visible(True)

# Customizing x-axis ticks
plt.xticks(list(range(0, len(bin_counts_data_addition), int(100/bin_size_data_addition))), list(range(50, 751, 100)))

# Annotating each bar with its value
for i, bar in enumerate(bars_data_addition):
    yval = bar.get_height()
    if yval != 0:  # Only annotate bars that have a value
        plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f"({bin_labels_data_addition[i]},{yval})", ha='center', va='bottom', rotation=45)

plt.xlabel("Number of Cycles")
plt.ylabel("Frequency")
plt.title("Data addition with integers 5 times $10^4$ trials")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
