import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["A", "B", "C", "D"]
values = [10, 24, 36, 40]

# Hatch patterns
patterns = ["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]

# Plotting
fig, ax = plt.subplots()

bars = ax.bar(categories, values, color="blue")

# Apply hatch patterns to each bar
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart with Hatch Patterns")

# Show plot
plt.show()
