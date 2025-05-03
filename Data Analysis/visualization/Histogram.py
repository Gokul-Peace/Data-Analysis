import matplotlib.pyplot as plt

ages = [23, 25, 22, 30, 28, 35, 40, 21, 22, 23, 29, 26, 33, 38, 27, 25, 24, 36, 31, 30]

plt.hist(ages,bins=5, edgecolor='black')
plt.title("Age Distribution")
plt.show()