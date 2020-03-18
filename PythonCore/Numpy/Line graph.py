import numpy as np
import matplotlib.pyplot as plt

x = [0, 1] #x轴
y = [0, 1] #y轴
plt.figure()#创建绘图对象
plt.ylabel('ACC@1',size=20)#y轴的坐标 size为字体大小
plt.xlabel('Iters',size=20)#x轴的坐标
plt.title('line',size=30)#标题
plt.plot(x, y,linewidth=3,c='g')#在当前对象进行绘图,c为颜色,linewidth为线的宽度
plt.show()  #将当先图像显示出来
plt.savefig("1.jpg")#将图像保存下来
