import turtle
colors=['blue','black','red','yellow','green']
turtle.pensize(10)

for i in range(5):
    turtle.pencolor(colors[i])
    if i<3:
        #绘制上三个环
        turtle.goto(120*i,0)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
    else:
        #下两个环
        turtle.goto(60+120*(i-3),-50)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
turtle.done()
