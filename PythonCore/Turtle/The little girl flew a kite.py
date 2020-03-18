import turtle as t
import random

# 画心
def xin():
    def curvemove():
        for i in range(200):
            t.right(1)
            t.forward(0.5)
            t.color('red', 'red')
            t.begin_fill()
            t.left(140)
            t.forward(60)
            curvemove()
            t.left(120)
            curvemove()
            t.forward(60)
            t.end_fill()

# 心里面的十字
def shizi():
    t.pu()
    t.goto(170,285)
    t.seth(0)
    t.pd()
    t.color("black","black")
    t.circle(1.5)
    t.pensize(2)
    t.fd(55)
    t.pensize(4)
    t.circle(1.5)
    t.pu()
    t.seth(-90)
    t.goto(198,295)
    t.seth(-90)
    t.pensize(2)
    t.pd()
    t.fd(65)
    t.circle(1.5)
    t.circle(160,40)
    t.circle(-130,27)
    t.circle(-60,40)
    t.circle(80,60)
# 夹子
def jiazi2():
    def jiazi(angle):
        t.pd()
        t.pensize(1)
        t.color("black","brown")
        t.begin_fill()
        t.seth(angle)
        t.fd(20)
        t.seth(angle-240)
        t.fd(10)
        t.seth(angle-120)
        t.fd(20)
        t.seth(angle-240)
        t.fd(10)
        t.end_fill()
        t.pu()
# 画夹子
    t.pu()
    t.goto(216,180)
    jiazi(180)
    t.goto(230,150)
    jiazi(200)
    t.goto(250,125)
    jiazi(220)
    t.goto(265,95)
    jiazi(200)
    t.goto(275,55)
    jiazi(160)
# 人
def people():
    t.pensize(2)
# 皇冠
def huangguan():
        t.pu()
        t.goto(-200,0)
        t.color("gold","gold")
        t.pd()
        t.begin_fill()
        t.seth(120)
        t.fd(32)
        t.seth(-120)
        t.fd(15)
        t.seth(150)
        t.fd(10)
        t.seth(-120)
        t.fd(10)
        t.seth(160)
        t.fd(15)
        t.seth(-60)
        t.fd(32)
        t.seth(50)
        t.circle(-40,60)
        t.end_fill()
# 脸
def face():
    t.pu()
    t.goto(-212,-3)
    t.color("black","white")
    t.pd()
    t.circle(-40,150)

# 头发
def hair():
    t.pu()
    t.color("black","black")
    t.goto(-212, -3)
    angle = -160
for i in range(32):
    t.pd()
    angle+= 1.4
    t.seth(angle)
    t.circle(60, 50)
    t.fd(random.randint(40,45))
    t.pu()
    t.goto(-212, -3)
    angle = -50
for i in range(32):
    t.pd()
    angle -= 1.5
    t.seth(angle)
    t.circle(-60, 50)
    t.fd(random.randint(38,40))
    t.pu()
    t.goto(-212, -5)

# 脖子
def nick():
    t.pu()
    t.goto(-200,-78)
    t.pd()
    t.seth(-90)
    t.fd(10)
    t.seth(-45)
    t.fd(20)
    t.seth(180)
    t.fd(30)
    t.seth(55)
    t.fd(15)
    t.circle(10,80)

# 下半身
def body():
    t.pu()
    t.goto(-185,-100)
    t.seth(-65)
    t.pd()
    for i in range(120):
        t.fd(1.5)
        t.right(0.1)
        t.seth(220)
        t.circle(-130,70)
        t.seth(75)
    for i in range(130):
        t.fd(1.5)
        t.right(0.06)
# 腿
def leg():
        t.pu()
        t.goto(-220,-300)
        t.pd()
        t.seth(-90)
        t.fd(80)
        t.pensize(5)
        t.color("red","red")
        t.fd(8)
        t.seth(-30)
        t.pensize(6)
        t.color("black","black")
        t.fd(5)
        t.pu()
        t.pensize(2)
        t.goto(-185,-300)
        t.pd()
        t.seth(-90)
        t.fd(80)
        t.pensize(5)
        t.color("red","red")
        t.fd(8)
        t.seth(-30)
        t.pensize(6)
        t.color("black","black")
        t.fd(5)
huangguan()
face()
nick()
body()
leg()
hair()

# 手
t.pu()
t.goto(-190,-165)
t.pensize(2)
t.pd()
t.seth(49)
t.fd(160)
t.circle(-10,80)

# 眼睛
t.pu()
t.goto(-185,-30)
t.seth(90)
t.pd()
t.circle(5,180)

# 星星
def star(x,y):
    color = ["blue","yellow","red","gold","orange","pink","green","purple"]
    t.pencolor(random.choice(color))
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(90)
    t.fd(8)
    t.bk(4)
    t.seth(0)
    t.fd(4)
    t.bk(8)
    t.fd(4)
    t.seth(45)
    t.fd(4)
    t.bk(8)
    t.fd(4)
    t.seth(-45)
    t.fd(4)
    t.bk(8)

if __name__ == "__main__":
    t.pensize(4)# 设置画笔的大小
    t.color("black")# 设置画笔颜色和填充颜色(pink)
    t.setup(650, 800)# 设置主窗口的大小为600*800
    t.speed(10)# 设置画笔速度为10
    t.pu()
    t.goto(200, 220)
    t.pd()

# 心
xin()
# 十字
shizi()
# 夹子
jiazi2()

#线
t.pu()
t.goto(198,280)
t.pd()
t.seth(-120)
t.circle(-1100,22)
t.circle(20,90)
t.circle(-30,50)
t.circle(15,60)

# 人
people()

# 裙子上的点点
star(-230, -200)
star(-220, -180)
star(-200, -150)
star(-180, -288)
star(-160, -250)
star(-210, -150)
star(-210, -140)
for i in range(10):
    star(random.randint(-205,-170),random.randint(-300,-200))

# 隐藏画笔
t.ht()
t.done()

