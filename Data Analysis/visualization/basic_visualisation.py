import matplotlib.pyplot as plt

# Sample data
students = ["Alice", "Bob", "Charlie", "David","gokul"]
scores = [85, 92, 78, 90,100]

# Create a bar chart
# plt.bar(students,scores)

# # Add labels and title
# plt.xlabel("Students")
# plt.ylabel("scores")
# plt.title("Student Test Scores")

# plt.show()

# Explanation:
# plt.bar() → creates the bar chart.
# plt.xlabel() / plt.ylabel() → add axis labels.
# plt.title() → adds a chart title.
# plt.show() → displays the chart window.

# Save instead of show
# plt.savefig("bar_chart.png")




# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 7]

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Values')

# Add title and labels
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()