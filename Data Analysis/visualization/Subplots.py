import matplotlib.pyplot as plt

# plot 1
years = [2015, 2016, 2017, 2018, 2019, 2020]
temperature = [30.5, 32.1, 31.3, 29.8, 30.0, 31.5]

# plot 2
products = ['Laptops', 'Mobiles', 'Tablets', 'Accessories']
sales = [150, 300, 100, 80]

#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(1,2,1)
plt.plot(years,temperature,marker="o")

plt.subplot(1,2,2)
plt.plot(products,sales)
# plt.figure(figsize=(10, 4)) can also set figsize if it looks cramped:
plt.show()
# plt.savefig("plot.png")