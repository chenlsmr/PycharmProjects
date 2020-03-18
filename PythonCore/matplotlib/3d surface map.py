import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection

data = np.random.randint(100,500,(3,10,20))
x,y,z = data[0],data[1],data[2]  # numpy同时生成三维数据
fig = plt.figure()
ax1 = fig.add_subplot(121,projection='3d')
ax1.plot_surface(x,y,z,cmap=plt.cm.winter,rstride=1,cstride=1) # rstride和cstride是隔几行几列取一个数字，代表曲面的稀疏度
ax2 = fig.add_subplot(122,projection='3d')
ax2.plot_surface(x,y,z,cmap=plt.cm.winter,rstride=10,cstride=10)
plt.show()
