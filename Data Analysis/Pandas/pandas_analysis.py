# 🐼 Getting Started with Pandas
# First, make sure Pandas is installed:
# pip install pandas

# Now let’s read the same CSV using Pandas:
import pandas as pd

# Read the CSV file
df = pd.read_csv("sample_data.csv")

# Show the first few rows
print(df.head())

#print all rows
print(df)


# Show column names
print(df.columns)

# Access one column
print(df["Name"])

# Describe the numerical columns
print(df.describe())

# Filter rows (age > 28)
print(df[df["Age"] > 28])


# 🧪 Mini Task (Try This):
# 1. Load the CSV into a DataFrame
# 2. Print only the names of people from "Delhi"
# 3. Find the average age
# 4. Save only "Name" and "City" columns to a new CSV

# Load the CSV into a DataFrame
print(pd.DataFrame(df))

# Print only the names of people from "Delhi"
print(df[df["City"] == "Delhi"])

# Find the average age
print(df.describe().mean())

#Save only "Name" and "City" columns to a new CSV
# index=False ensures the row numbers (index) are not written to the file
df[["Name", "City"]].to_csv("new.csv", index=False)



# Some powerful practice exercises
# Sorting Data
# Use case: Ranking, organizing.
print(df.sort_values(by = "Name",ascending = True))

# ✅ 3. Adding a New Column
# Add a new column 'Senior' for people aged 30 and above
# Use case: Create derived attributes.
df["senior"] = df["Age"] >= 35
print(df)

 # Handling Missing Data
# Use case: Cleaning real-world messy data.

# Simulate a missing value
df.loc[2, "City"] = None

# Fill missing city with 'Unknown'
df["City"] = df["City"].fillna("Unknown")
print(df)


# Merging with Another Dataset
# Extra info
data2 = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Salary": [50000, 60000, 70000, 65000]
}
df2 = pd.DataFrame(data2)

# Merge with original
merged = pd.merge(df, df2, on="Name")
print(merged)
