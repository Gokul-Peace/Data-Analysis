import matplotlib.pyplot as plt


years = [2015, 2016, 2017, 2018, 2019, 2020]
temperature = [30.5, 32.1, 31.3, 29.8, 30.0, 31.5]

plt.plot(years,temperature,marker="o",linestyle="-",color='green')

plt.title("Years vs Temperature")
plt.xlabel("Years")
plt.grid(True)
plt.ylabel("Temperature")
plt.show()