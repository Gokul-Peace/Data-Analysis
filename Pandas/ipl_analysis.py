import pandas as pd


# Load the IPL dataset from a CSV file
df = pd.read_csv("Data sets/Cricket_data.csv")



                                        # --- Basic Exploration ---


# Display basic info

# Display the first 5 rows of the dataset to get a quick overview
print(df.head())

# Print the names of all columns in the dataset
# This helps understand what data is available and how it is labeled
print(df.columns)

# Print a concise summary of the DataFrame
# Includes number of non-null entries, data types, and memory usage
print(df.info)



                                        # --- Data Cleaning ---

# This allows for time-based filtering and analysis
data = df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
print(data)



                                        # --- Analysis ---

# Count how many times each team has won
# Helps identify top-performing teams
print(f"Match wins by team:{df["winner"].value_counts()}")


# Count how many matches were played in each IPL season
# Useful for tracking the number of matches over the years
print(f"Matches per season:{df["season"].value_counts()}")

# Most popular venues
print(f"Top venues by Matches hosted: {df["venue_name"].value_counts().head(10)}")

# Top POM winners
print(f"Top Player of the Match awards: {df["pom"].value_counts()}")

# ✅ 1. groupby() + count()
# Count how many matches each team played as the home team
print(df.groupby("home_team")["id"].count().reset_index(name="match_count"))

# Use case: Count non-null values (e.g., matches per team).
# How it works: Groups the DataFrame by home_team, then counts the number of entries in the "id" column for each group.
# Why use reset_index()? Converts the groupby result into a normal DataFrame.


# ✅ 2. groupby() + mean()

# Find average first innings score for each team when they played at home
print(df["1st_inning_score"].unique())

# Step 1: Extract runs before '/' and convert to integer
df["1st_inning_runs"] = df["1st_inning_score"].str.extract(r"(\d+)").astype(float)


# Step 2: Now you can safely do mean()
print(df.groupby("home_team")["1st_inning_runs"].mean().reset_index(name="avg_1st_inning_runs"))

# Use case: Find the average of a numeric column grouped by categories (e.g., team, season).
# How it works: Calculates the mean of "1st_inning_score" for each home_team.

# ✅ 3. groupby() + sum()
# Total home team runs for each IPL season
print(df.groupby("season")["home_runs"].sum().reset_index(name="total_home_runs"))

# Use case: Sum values (e.g., total runs or scores per season).
# How it works: Groups by season and sums the home_runs for each.


# ✅ 4. groupby() + agg() (Multiple Aggregations)

# For each winning team, get average home/away runs and number of wins
print(df.groupby("winner").agg({
    "home_runs": "mean",     # average home runs
    "away_runs": "mean",     # average away runs
    "id": "count"            # number of wins
}).reset_index().rename(columns={"id": "total_wins"}))

# Use case: Apply multiple functions (mean, sum, count, etc.) to different columns in one go.
# How it works: agg() takes a dictionary where keys are columns and values are aggregation functions.

# ✅ 5. groupby().size()
# Count number of matches per venue
print(df.groupby("venue_name").size().reset_index(name="match_count"))

# Use case: Quickly count the number of records in each group.
# How it works: Similar to .count() but counts total rows, not specific columns.



# ✅ 6. value_counts() vs groupby().size()

# Using value_counts
print(df["venue_name"].value_counts().reset_index(name="venue count"))

# Same with groupby
print(df.groupby("venue_name").size().sort_values(ascending=False))

# Use case: Both return frequencies. value_counts() is faster for a single column; groupby().size() is more flexible and can be chained.

# ✅ 7. reset_index()
# Resetting index after groupby to turn the result into a usable DataFrame
print(df.groupby("winner").size().reset_index(name="win_count"))