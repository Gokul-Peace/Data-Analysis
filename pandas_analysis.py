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
