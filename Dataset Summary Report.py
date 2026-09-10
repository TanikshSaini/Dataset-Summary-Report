# Step 1: Import Libraries
import pandas as pd

# Step 2: Load Dataset
# Replace with the actual file path from your LMS Study Material tab
df = pd.read_csv("your_dataset.csv")

# Step 3: Inspect Dataset
print("🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Last 5 Rows:")
print(df.tail())

print("\n🔹 Random Sample (10 rows):")
print(df.sample(10))

# Step 4: Dataset Structure
print("\nDataset Shape (rows, columns):", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nIndex:", df.index)
print("\nData Types:\n", df.dtypes)

# Step 5: Summary Statistics
print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Descriptive Statistics:")
print(df.describe(include='all'))

# Step 6: Missing Values
print("\n🔹 Missing Values per Column:")
print(df.isnull().sum())
