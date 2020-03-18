import turtle
import time


def head():
    # 配置画笔属性
    turtle.fillcolor("black")
    turtle.color("black")
    turtle.colormode(255)
    turtle.speed(1)

    # 绘制母企鹅头部
    turtle.penup()
    turtle.goto(-300, 350)
    turtle.seth(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(-200, -110)
    turtle.penup()
    turtle.goto(-300, 350)
    turtle.pendown()
    turtle.seth(0)
    turtle.circle(-200, 110)
    turtle.seth(213)
    turtle.circle(-345, 66)
    turtle.end_fill()


def lefteye():
    # 配置画笔属性
    turtle.Turtle().screen.delay(0)
    turtle.fillcolor("white")
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制母企鹅的左眼
    turtle.pu()
    turtle.goto(-350, 275)
    turtle.seth(180)
    turtle.pd()
    turtle.begin_fill()

    # 画椭圆
    a = 1.0
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)  # 向左转3度
            turtle.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()

    # 绘制左眼眼影
    turtle.begin_fill()
    turtle.fillcolor("pink")
    turtle.pu()
    turtle.goto(-378, 255)
    turtle.pendown()
    turtle.color("pink")
    turtle.seth(15)
    turtle.circle(-100, 35)
    turtle.pu()
    turtle.goto(-350, 275)
    turtle.seth(180)
    a = 1
    for i in range(20):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.goto(-350, 275)
    turtle.seth(0)
    a = 1
    for i in range(20):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.rt(3)
            turtle.fd(a)
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()

    # 绘制睫毛
    turtle.pu()
    turtle.goto(-350, 275)
    turtle.seth(180)
    turtle.pd()
    a = 1
    for i in range(20):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.pensize(3)
    turtle.color(242, 156, 177)
    turtle.circle(-20, 190)
    turtle.pensize(1)

    # 绘制母企鹅的左眼珠
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(-330, 245)
    turtle.seth(180)
    turtle.pd()
    turtle.begin_fill()
    a = 0.01
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.05
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.05
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()


def righteye():
    # 配置画笔属性
    turtle.Turtle().screen.delay(0)
    turtle.fillcolor("white")
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制母企鹅的右眼
    turtle.pu()
    turtle.goto(-250, 275)
    turtle.seth(180)
    turtle.pd()
    turtle.begin_fill()

    a = 1.0
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()

    # 绘制右眼眼影
    turtle.begin_fill()
    turtle.fillcolor("pink")
    turtle.pu()
    turtle.goto(-278, 255)
    turtle.pendown()
    turtle.color("pink")
    turtle.seth(15)
    turtle.circle(-100, 35)
    turtle.pu()
    turtle.goto(-250, 275)
    turtle.seth(180)
    a = 1
    for i in range(20):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.goto(-250, 275)
    turtle.seth(0)
    a = 1
    for i in range(20):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.rt(3)
            turtle.fd(a)
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()

    # 绘制睫毛
    turtle.pu()
    turtle.goto(-250, 275)
    turtle.seth(0)
    turtle.pd()
    a = 1
    for i in range(20):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.rt(3)  # 向左转3度
            turtle.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.pensize(3)
    turtle.color(242, 156, 177)
    turtle.circle(20, 190)
    turtle.pensize(1)

    # 绘制母企鹅的右眼珠
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(-270, 245)
    turtle.seth(180)
    turtle.pd()
    turtle.begin_fill()
    a = 0.01
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.05
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.05
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()


def mouth():
    # 配置画笔属性
    turtle.fillcolor((250, 175, 8))
    turtle.color((250, 175, 8))
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制母企鹅的嘴巴
    turtle.pu()
    turtle.goto(-410, 120)
    turtle.seth(30)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(-225, 60)
    turtle.circle(-8, 150)
    turtle.seth(210)
    turtle.circle(-225, 60)
    turtle.seth(-210)
    turtle.circle(-8, 150)
    turtle.pu()
    turtle.end_fill()


def bowknot():
    # 配置画笔属性
    turtle.speed(1)
    turtle.fillcolor("pink")
    turtle.pu()
    turtle.color("pink")
    turtle.goto(-250, 360)
    turtle.pd()
    turtle.seth(225)

    # 绘制蝴蝶结的上半部分
    turtle.begin_fill()
    turtle.fillcolor("pink")
    turtle.pu()
    turtle.goto(-250, 360)
    turtle.pd()
    turtle.circle(-70, 100)
    turtle.seth(50)
    turtle.circle(-80, 53)
    turtle.pu()
    turtle.goto(-250, 360)
    turtle.seth(50)
    turtle.pd()
    turtle.circle(70, 100)
    turtle.seth(225)
    turtle.circle(80, 53)
    turtle.end_fill()

    # 绘制蝴蝶结下半部分
    turtle.pu()
    turtle.goto(-195, 335)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor("pink")
    turtle.seth(45)
    turtle.circle(-70, 100)
    turtle.seth(230)
    turtle.circle(-80, 62.5)
    turtle.pu()
    turtle.goto(-195, 335)
    turtle.seth(225)
    turtle.pd()
    turtle.circle(70, 100)
    turtle.seth(50)
    turtle.circle(80, 58)
    turtle.end_fill()

    # 蝴蝶结的中间部分
    turtle.begin_fill()
    turtle.fillcolor("pink")
    turtle.pu()
    turtle.color("pink")
    turtle.goto(-255, 370)
    turtle.pd()
    turtle.seth(225)
    turtle.circle(40, 360)
    turtle.end_fill()


def scarf():
    # 配置画笔属性
    turtle.fillcolor("pink")
    turtle.color("pink")
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制围巾
    turtle.pu()
    turtle.goto(-489, 82)
    turtle.seth(-115)
    turtle.pd()
    turtle.begin_fill()
    turtle.fd(75)
    turtle.seth(-30)
    turtle.circle(450, 10)
    turtle.seth(-90)
    turtle.fd(100)
    turtle.seth(-35)
    turtle.circle(50, 70)
    turtle.seth(90)
    turtle.fd(95)
    turtle.seth(-12)
    turtle.circle(450, 40)
    turtle.seth(110)
    turtle.fd(70)
    turtle.seth(213)
    turtle.circle(-345, 64)
    turtle.pu()
    turtle.end_fill()


def body():
    # 配置画笔属性
    turtle.fillcolor("black")
    turtle.color("black")
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制母企鹅的身体
    turtle.pu()
    turtle.goto(-489, 82)
    turtle.seth(-115)
    turtle.pd()
    turtle.begin_fill()
    turtle.fd(175)
    turtle.circle(120, 40)
    turtle.seth(30)
    turtle.circle(200, 40)
    turtle.seth(-90)
    turtle.circle(174, 180)
    turtle.seth(-70)
    turtle.circle(200, 40)
    turtle.seth(70)
    turtle.circle(120, 43)
    turtle.fd(175)
    turtle.seth(213)
    turtle.circle(-345, 66)
    turtle.pu()
    turtle.end_fill()


def feet():
    # 配置画笔属性
    turtle.fillcolor((250, 175, 8))
    turtle.color((250, 175, 8))
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制母企鹅的左脚
    turtle.pu()
    turtle.goto(-300, -228)
    turtle.seth(180)
    turtle.pd()
    turtle.begin_fill()
    turtle.fd(200)
    turtle.circle(-10, 120)
    turtle.circle(-120, 40)
    turtle.pu()
    turtle.end_fill()

    # 绘制母企鹅的右脚
    turtle.pu()
    turtle.goto(-300, -228)
    turtle.seth(0)
    turtle.pd()
    turtle.begin_fill()
    turtle.fd(200)
    turtle.circle(10, 120)
    turtle.circle(120, 50)
    turtle.pu()
    turtle.end_fill()


def belly():
    # 配置画笔属性
    turtle.fillcolor("white")
    turtle.color("white")
    turtle.speed(1)
    turtle.colormode(255)

    # 绘制母企鹅的白色肚皮
    turtle.pu()
    turtle.goto(-305, 28)
    turtle.seth(180)
    turtle.pd()
    turtle.begin_fill()

    # 画椭圆
    a = 4.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.1
            turtle.lt(3)
            turtle.fd(a)
        else:
            a = a - 0.1
            turtle.lt(3)
            turtle.fd(a)
    turtle.pu()
    turtle.end_fill()
    turtle.pu()
    turtle.end_fill()


turtle.Turtle().screen.delay(0)

head();
bowknot();
lefteye();
righteye();
mouth();
feet();
body();
belly();
scarf();
turtle.hideturtle()
turtle.mainloop()