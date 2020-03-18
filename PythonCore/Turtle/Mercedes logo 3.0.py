import turtle as t
import time
R = 150
r = R - 10

t.pensize(10)
t.color("black","white")
t.speed(10)
t.circle(R,360) # 画圆圈
t.penup()
t.left(90)
t.forward(R)
t.pensize(1)
t.pendown()
t.forward(R)
t.pensize(1)
t.fillcolor("black")
# 左侧三角形
t.begin_fill()
t.left(170)
t.forward(r)
t.right(180)
t.forward(r)
t.right(170)
t.forward(R)
t.right(60)
t.forward(R)
t.right(170)
t.forward(r)
t.end_fill()
# 下面三角形
t.right(180)
t.forward(r)
t.begin_fill()
t.left(160)
t.forward(r)
t.right(180)
t.forward(r)
t.right(170)
t.forward(R)
t.right(60)
t.forward(R)
t.right(170)
t.forward(r)
t.end_fill()
# 右边三角形
t.right(180)
t.forward(r)
t.begin_fill()
t.left(160)
t.forward(r)
t.right(180)
t.forward(r)
t.right(170)
t.forward(R)
t.right(60)
t.forward(R)
t.right(170)
t.forward(r)
t.end_fill()

t.hideturtle() # 隐藏小海龟画笔
t.mainloop() # 保留图像