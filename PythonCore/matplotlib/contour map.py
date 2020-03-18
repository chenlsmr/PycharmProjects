import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection

x = np.arange(-10,10,0.01)  #生成步长为0.01的数据
y = np.arange(-10,10,0.01)
x,y=np.meshgrid(x,y)
def func(x,y):
    return x**2+y**2
fig,axes = plt.subplots(2,2)
axes[0,0].contour(x,y,func(x,y),20,cmap=plt.cm.winter,alpha=0.8) # 不填充，只是线20是指分成20等份，分太多会看不清
axes[0,1].contourf(x,y,func(x,y),20,cmap=plt.cm.hot)  # 填充
c = axes[1,0].contour(x,y,func(x,y),[8,20],c='k')  # [8,20]是只想看这两条线
plt.clabel(c,inline=True,fontsize=10,fmt='%.f',colors=['k','y']) # 设置数据标签格式，inline是在线上
d = axes[1,1].contourf(x,y,func(x,y),10,cmap=plt.cm.hot)
plt.clabel(d,inline=True,fontsize=10,fmt='%.f')
plt.colorbar(d)# 显示数据条
plt.xticks(())
plt.yticks(())# 去除坐标轴
plt.show()
