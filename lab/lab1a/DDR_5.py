import matplotlib.pyplot as plt

bin_counts_led = [
85,0,0,0,0,0,0,7156,781,19,3,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,1862,
41,26,2,0,0,0,8,0,1,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,]
min = 83
max = 871
binSize = 7
# Correcting the bins for the LED data to match the counts
bins_led_corrected = [min + i*binSize for i in range(len(bin_counts_led))]

# Plotting the histogram for "Turn on or off Led 5 times 10^4 trials"
plt.figure(figsize=(10, 6))
bars_led = plt.bar(bins_led_corrected, bin_counts_led, align='edge', width=12*0.9, edgecolor="k", alpha=0.7, color='skyblue')

# Annotating each bar with its value
for bar in bars_led:
    yval = bar.get_height()
    if yval != 0:  # Only annotate bars that have a value
        plt.text(bar.get_x() + bar.get_width()/2, yval + 20, f'({int(bar.get_x())},{yval})', ha='center', va='bottom', rotation=45, fontsize=8)

# Adjusting the x-axis for clarity
plt.xticks([i for i in range(((min//100)+1)*100, ((max//100)+1)*100, 81)])
plt.xlabel("Number of Cycles")
plt.ylabel("Frequency")
plt.title("Read a word from DDR2 5 times $10^4$ trials")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
