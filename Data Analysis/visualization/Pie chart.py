import matplotlib.pyplot as plt


categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Utilities']
expenses = [12000, 6000, 2000, 3000, 1500]
myexplode = [0.2, 0, 0, 0,0]
mycolors = ["black", "hotpink", "b", "#4CAF50","r"]

plt.pie(expenses,labels=categories,explode=myexplode,startangle=190,shadow=True,colors=mycolors,autopct='%1.1f%%')
plt.title(" Pie Chart – Monthly Expenses")
plt.legend(title="categories")
plt.show()