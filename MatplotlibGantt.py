from matplotlib import pyplot as plt


plt.ylim(0, 50)
plt.xlim(0, 50)
plt.broken_barh([(20, 10), (20, 5)], (20, 10), facecolors="tab:orange")
plt.broken_barh([(10, 10), (30, 10)], (10, 9), facecolors="tab:blue")

plt.show()
