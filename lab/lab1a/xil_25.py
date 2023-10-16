import matplotlib.pyplot as plt
bin_counts_led = [
305,155,33,5,5,6,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,12,8,4,9,51,127,113,53,17,18,29,34,3,1,1,1,0,0,1,0,0,1,1,0,0,1]
min = 236318
max = 7293533
binSize = 70572
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
plt.xticks([i for i in range(((min//100)+1)*100, ((max//100)+1)*100, 700000)])
plt.xlabel("Number of Cycles")
plt.ylabel("Frequency")
plt.title("print 10 char string with xil_printf() 25 times $10^3$ trials")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
