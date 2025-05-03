import matplotlib.pyplot as plt

products = ['Laptops', 'Mobiles', 'Tablets', 'Accessories']
sales = [150, 300, 100, 80]

plt.bar(products,sales,color="green",width=0.5)
plt.title("Bar Chart - sales by Product")
plt.xlabel("products")
plt.ylabel("sales")
plt.show()