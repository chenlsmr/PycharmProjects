import turtle as t
#-------------脸
t.setup(960,959,0,0)
t.color("orange")
t.pensize("25")
t.penup()
t.goto(-300,0)
t.pendown()
t.left(90)
t.fillcolor("yellow")
t.begin_fill ()
t.circle(-300)
t.end_fill ()

#-----------嘴-----------
t.penup()
t.goto(-220,-10)
t.seth(90)
for i in range(90):
    t.pensize(4+0.15*i)
    t.color("brown")
    t.pendown()
    t.circle(-220,-1)
for i in range(90):
    t.pensize(17.5-0.15*i)
    t.color("brown")
    t.pendown()
    t.circle(-220,-1)

#------------左眼---------------   
t.penup()
t.goto(-80,150)
t.color("orange")
t.pensize("25")
t.seth(90)
t.pendown()
t.left(50)
t.circle(200,80)
t.seth(270)
t.circle(200,15)

t.penup()
t.goto(-70,90)
t.color("orange")
t.pensize("25")
t.seth(90)
t.pendown()
t.left(50)
t.circle(200,65)
t.left(10)
t.circle(200,10)

t.penup()
t.goto(-70,150)
t.seth(270)
t.pendown()
t.circle(-200,15)

#-------------右眼----------------


t.penup()
t.goto(70,150)
t.color("orange")
t.pensize("25")
t.seth(90)
t.pendown()
t.right(50)
t.circle(-200,80)
t.seth(270)
t.circle(-200,15)

t.penup()
t.goto(70,90)
t.seth(90)
t.pendown()
t.right(50)
t.circle(-200,65)
t.right(10)
t.circle(200,10)

t.penup()
t.goto(70,150)
t.seth(270)
t.pendown()
t.circle(200,15)

t.penup()
t.pensize(5)
t.color("black")
t.goto(-300,125)
t.pendown()
t.seth(0)
t.fillcolor('black')
t.begin_fill()
t.circle(15,360)
t.end_fill()

t.penup()
t.pensize(5)
t.color("black")
t.goto(100,120)
t.pendown()
t.seth(0)
t.fillcolor('black')
t.begin_fill()
t.circle(15,360)
t.end_fill()


#----------左眉毛-----------------
t.penup()
t.goto(-70,200)
t.color("black")
t.pensize("25")
t.seth(90)
t.pendown()
t.left(30)
t.circle(200,60)


#----------右眉毛-----------------
t.penup()
t.goto(70,200)
t.color("black")
t.pensize("25")
t.seth(90)
t.pendown()
t.right(30)
t.circle(-200,60)


#---------左红-------------------
t.penup()
t.color("red")
t.goto(150,20)
t.pendown()
t.fillcolor ("red")
t.begin_fill ()
t.circle(20)
t.end_fill ()

#---------右红----------------
t.penup()
t.color("red")
t.goto(-180,20)
t.pendown()
t.fillcolor ("red")
t.begin_fill ()
t.circle(20)
t.end_fill ()

t.done()
