import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arrange(-5.0,5.0,0.1)
y = sigmoid(x)
# 画图
plt.plot(x,y)
plt.ylim(-0.1,1.1) #指定y轴的范围
plt.show()
