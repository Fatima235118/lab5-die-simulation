import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Roll a fair six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000)

# Print first 10 rolls
print("First 10 rolls:", rolls[:10])

# Count occurrences of each face
faces, counts = np.unique(rolls, return_counts=True)

# Calculate probabilities
empirical_probabilities = counts / 1000
theoretical_probability = 1 / 6

# Display results
print("\nFace Count Empirical P Theoretical P")

for face, count, empirical in zip(
    faces, counts, empirical_probabilities
):
    print(
        f"{face} {count} {empirical:.3f} "
        f"{theoretical_probability:.4f}"
    )

# Create histogram
plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black"
)

plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Fair Die Rolls - 1000 Simulations")
plt.xticks(range(1, 7))

# Save histogram
plt.savefig("die_rolls.png")
plt.close()

print("\nSaved die_rolls.png")