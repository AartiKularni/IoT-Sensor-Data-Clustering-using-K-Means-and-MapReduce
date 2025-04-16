import pandas as pd

# Load the dataset
df = pd.read_csv("sensor_data.csv")

# Drop non-numeric columns (like 'date', 'time' if present)
df = df.select_dtypes(include=['float64', 'int64'])

# Choose N rows for centroid seeds
N = 50

# First N rows → Centroid 1
centroid1 = df.iloc[:N].mean()

# Last N rows → Centroid 2
centroid2 = df.iloc[-N:].mean()

# Save to centroids.txt
with open("centroids.txt", "w") as f:
    f.write(",".join([str(round(x, 6)) for x in centroid1.values]) + "\n")
    f.write(",".join([str(round(x, 6)) for x in centroid2.values]) + "\n")

print("✅ centroids.txt generated successfully!")
