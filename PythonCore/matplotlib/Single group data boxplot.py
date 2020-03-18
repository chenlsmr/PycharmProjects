from matplotlib import pyplot as plt
dataArray=[5,6,2,4,8,9,10,2,4,5,3,5,15]
plt.boxplot(dataArray,labels=["A"])
plt.title("Box-plot Test")
plt.savefig("a.png")
plt.show()
