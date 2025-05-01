import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data sets/Cricket_data.csv")


# 🔹 IPL Visualization 1: Matches Played by Each Team (as Home Team)
 

# # Count how many times each team appeared as the home team
home_matches = df["home_team"].value_counts()

# Set the figure size for better readability
plt.figure(figsize=(10, 6))

# Create a bar chart from the match count
home_matches.plot(kind='bar', color='skyblue')

# Add title to the chart
plt.title("Number of Matches Played as Home Team")

# Label the x-axis
plt.xlabel("Team")

# Label the y-axis
plt.ylabel("Match Count")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()


# 🔹 IPL Visualization 2: Most Frequent Winners

# Count how many matches each team has won
wins = df["winner"].value_counts()

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart for match wins
wins.plot(kind='bar', color='lightgreen')

# Title of the chart
plt.title("Most Matches Won by Teams")

# X-axis label
plt.xlabel("Team")

# Y-axis label
plt.ylabel("Wins")

# Rotate team names on x-axis
plt.xticks(rotation=45)

# Adjust layout so labels don't get cut off
plt.tight_layout()

# Display the plot
plt.show()
