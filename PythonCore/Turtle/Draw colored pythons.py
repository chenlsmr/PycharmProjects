import turtle
turtle.setup(650,350,200,200)
colors=['purple','red','yellow','pink','blue','green']
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for i in range(5):
    turtle.pencolor(colors[i])
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.pencolor(colors[5])
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
