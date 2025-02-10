import matplotlib.pyplot as plt
regions = ["CUMILLA", "DHAKA", "KHULNA", "RANGPUR"]
sales_figure = [390000, 430000, 250000, 130000]
plt.bar(regions, sales_figure, color='BLUE')
plt.xlabel("Regions")
plt.ylabel("Sales Revenue in BDT")
plt.title("Sales Revenue Comparison Across Regions")
for i, value in enumerate(sales_figure):
    plt.text(i, value + 50000, f"{value:,}", ha='center', fontsize=13, fontweight='bold')
plt.show()