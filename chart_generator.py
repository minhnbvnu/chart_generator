import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
metrics = ["Precision", "Recall", "F1", "MCC"]
models = [
    "DeepSmells",
    "DeepSmells-BiLSTM",
    "GRACOS-RGCN",
    "GRACOS-FastGCN",
    "GRACOS-RGAT",
]
data = [
    [
        [0.9181, 0.4630, 0.6156, 0.2687],
        [0.9406, 0.4225, 0.5831, 0.1912],
        [0.8366, 0.5984, 0.6977, 0.3741],
        [0.8858, 0.5527, 0.6807, 0.4150],
    ],
    [
        [0.9275, 0.4585, 0.6137, 0.2636],
        [0.9390, 0.4360, 0.5955, 0.2331],
        [0.7993, 0.6209, 0.6989, 0.3902],
        [0.8127, 0.5913, 0.6846, 0.4302],
    ],
    [
        [0.7032, 0.7271, 0.7150, 0.5729],
        [0.8594, 0.7263, 0.7873, 0.6955],
        [0.7355, 0.6750, 0.7040, 0.5316],
        [0.8157, 0.7338, 0.5022, 0.4967],
    ],
    [
        [0.7025, 0.7040, 0.7032, 0.5586],
        [0.8547, 0.7413, 0.7940, 0.7019],
        [0.6976, 0.6177, 0.6552, 0.4611],
        [0.7812, 0.4444, 0.5666, 0.4900],
    ],
    [
        [0.8150, 0.5160, 0.6320, 0.5320],
        [0.9200, 0.7750, 0.8410, 0.7750],
        [0.8030, 0.3940, 0.5280, 0.4130],
        [0.8040, 0.3290, 0.4670, 0.4240],
    ],
]

# Hatch patterns for each model
patterns = ["/", "..", "O", "\\", "*"]

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plotting each chart
for i in range(2):
    for j in range(2):
        ax = axs[i, j]
        for idx, model in enumerate(models):
            x = np.arange(len(metrics))  # the label locations
            width = 0.15  # the width of the bars
            offset = (idx % 5) * width
            bars = ax.bar(
                x + offset,
                data[idx][i * 2 + j],
                width=width,
                label=model,
                color="white",
                edgecolor="black",
                hatch=patterns[idx],
                alpha=0.8,
            )

        # Set chart titles
        if i == 0 and j == 0:
            ax.set_title("Complex Method", fontsize=25)
        elif i == 0 and j == 1:
            ax.set_title("Complex Conditional", fontsize=25)
        elif i == 1 and j == 0:
            ax.set_title("Feature Envy", fontsize=25)
        elif i == 1 and j == 1:
            ax.set_title("Multifaceted Abstraction", fontsize=25)

        ax.set_xticks(x + 0.3 * 2)  # Adjusted positions for the centering of bars
        ax.set_xticklabels(
            metrics, rotation=45, ha="right", fontsize=18
        )  # Use the correct metrics labels here
        ax.tick_params(axis="y", labelsize=18)

        ax.legend().set_visible(False)  # Hide individual legends

# Create a common legend with patterns and labels
legend_elements = []
for idx, pattern in enumerate(patterns):
    if pattern == "/":
        # Create a custom legend handle for '/'
        rect = Patch(facecolor="white", edgecolor="black", hatch="//")
        legend_elements.append(rect)
    elif pattern == "\\":
        # Create a custom legend handle for '-'
        rect = Patch(facecolor="white", edgecolor="black", hatch="\\\\")
        legend_elements.append(rect)
    else:
        # For other patterns, use Patch objects
        legend_elements.append(
            Patch(facecolor="white", edgecolor="black", hatch=pattern)
        )

# Add the legend to the figure
fig.legend(
    handles=legend_elements,
    labels=models,
    loc="center",
    bbox_to_anchor=(0.5, 0.5),
    ncol=3,
    fontsize=20,
)

# Adjust layout and display
plt.tight_layout()
plt.show()
