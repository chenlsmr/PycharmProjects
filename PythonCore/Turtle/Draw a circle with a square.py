import turtle
for i in range(360):#360 个正方形每隔 1 度排列
    turtle.setheading(i)
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)