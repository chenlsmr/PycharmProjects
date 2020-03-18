import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection

x= np.linspace(5,20,20)
y = np.linspace(20,100,20)
x1,y1 = np.meshgrid(x,y)
z = np.sin(x1)*y1+np.sin(y1)*x1  # 函数构造数据
fig = plt.figure()
ax1 = fig.add_subplot(121,projection='3d')
ax1.scatter(x1,y1,z,c='y',marker='D')
ax2 = fig.add_subplot(122,projection='3d')
ax2.scatter(x1[:10],y1[:10],z[:10],cmap=plt.cm.winter,marker='o')
ax2.scatter(x1[10:],y1[10:],z[10:],cmap=plt.cm.spring,marker='*')
plt.show()
