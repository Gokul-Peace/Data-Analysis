import matplotlib.pyplot as plt

height = [150, 160, 165, 170, 175, 180, 185]
weight = [50, 55, 60, 65, 70, 75, 80]

plt.scatter(height,weight,color = 'green',s=200,alpha=0.2)

plt.title("Height vs Weight")
plt.xlabel("height")
plt.ylabel("weight")
plt.show()