import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from mpl_toolkits.mplot3d.axes3d import Axes3D

# 绘制3维的散点图
x = np.random.randint(0, 10, size=100)
y = np.random.randint(-20, 20, size=100)
z = np.random.randint(0, 30, size=100)

# 此处fig是二维
fig = plt.figure()

# 将二维转化为三维
axes3d = Axes3D(fig)

# axes3d.scatter3D(x,y,z)
# 效果相同
axes3d.scatter(x, y, z)

