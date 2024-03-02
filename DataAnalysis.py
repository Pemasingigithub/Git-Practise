import pandas as pd
import matplotlib.pylab as plt
x = pd.array(["Apple", "Orange", "Mango", "Banana"])
y = pd.array([30, 20, 40, 32])
plt.bar(x, y)
plt.title("Fruits data Analysis")
plt.xlabel("Fruits Name")
plt.ylabel("Quantity of Fruits")
plt.show()
plt.barh(x, y)
plt.title("Fruits data Analysis")
plt.xlabel("Fruits Name")
plt.ylabel("Quantity of Fruits")
plt.show()
