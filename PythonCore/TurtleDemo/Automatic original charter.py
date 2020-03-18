# 导入turtle包的所有内容:
from turtle import *
#reset()
# 建立画布

for i in range(0, 360, 10):
    circle(100)  # 画圆
    left(10)  # 画完后左转10degree
    
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
