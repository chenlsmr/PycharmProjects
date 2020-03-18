import turtle

def head():
    turtle.color('black')
    # 脸轮廓
    turtle.fillcolor('#FFE4B5')
    turtle.begin_fill()
    # 落笔
    turtle.pd()
    # 画一个半径为指定值的圆
    turtle.circle(50)
    # 提笔
    turtle.pu()
    turtle.end_fill()
    # 移动到指定坐标位置，参数 1 代表 x 轴位置，参数 2 代表 y 轴位置
    turtle.goto(50, 60)
    turtle.pd()
    turtle.circle(25, 255)
    turtle.pu()
    turtle.goto(60, 80)
    turtle.pd()
    turtle.circle(-10, -200)
    turtle.pu()
    turtle.goto(-50, 60)
    turtle.pd()
    # 按逆时针改变行进方向
    turtle.seth(180)
    turtle.circle(-25, 255)
    turtle.pu()
    turtle.goto(-60, 80)
    turtle.pd()
    turtle.circle(10, -200)
    turtle.pu()
    # 眼睛
    turtle.goto(10, 65)
    turtle.seth(45)
    turtle.pd()
    turtle.circle(-8, 360)
    turtle.pu()
    turtle.goto(13, 62)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(-4, -360)
    turtle.pu()
    turtle.end_fill()
    turtle.goto(-10, 65)
    turtle.seth(135)
    turtle.pd()
    turtle.circle(8, 360)
    turtle.pu()
    turtle.goto(-13, 62)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(4, 360)
    turtle.pu()
    turtle.end_fill()
    # 鼻子
    turtle.goto(-6, 45)
    turtle.seth(70)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(-6, 150)
    turtle.pu()
    turtle.end_fill()
    turtle.goto(-6, 45)
    turtle.seth(-70)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(6, 150)
    turtle.pu()
    turtle.end_fill()
    # 嘴
    turtle.goto(0, 40)
    turtle.seth(270)
    turtle.pd()
    turtle.forward(7)
    turtle.pu()
    turtle.seth(200)
    turtle.pd()
    turtle.circle(-15, 60)
    turtle.pu()
    turtle.goto(0, 33)
    turtle.seth(-20)
    turtle.pd()
    turtle.circle(15, 60)
    turtle.pu()
    # 牙齿
    turtle.goto(0, 33)
    turtle.seth(270)
    turtle.pd()
    turtle.forward(13)
    turtle.seth(180)
    turtle.forward(6)
    turtle.seth(90)
    turtle.forward(13)
    turtle.pu()
    turtle.goto(6, 33)
    turtle.seth(270)
    turtle.pd()
    turtle.forward(13)
    turtle.seth(180)
    turtle.forward(6)
    turtle.pu()
    # 胡子
    turtle.goto(30, 30)
    turtle.seth(8)
    turtle.pd()
    turtle.circle(-40, 40)
    turtle.pu()
    turtle.goto(30, 25)
    turtle.seth(-5)
    turtle.pd()
    turtle.circle(-40, 40)
    turtle.pu()
    turtle.goto(30, 20)
    turtle.seth(-18)
    turtle.pd()
    turtle.circle(-40, 40)
    turtle.pu()
    turtle.goto(-30, 30)
    turtle.seth(172)
    turtle.pd()
    turtle.circle(40, 40)
    turtle.pu()
    turtle.goto(-30, 25)
    turtle.seth(188)
    turtle.pd()
    turtle.circle(40, 40)
    turtle.pu()
    turtle.goto(-30, 20)
    turtle.seth(196)
    turtle.pd()
    turtle.circle(40, 40)
    turtle.pu()


def hat():
    turtle.goto(-20, 97)
    turtle.pd()
    turtle.seth(80)
    turtle.forward(20)
    turtle.seth(60)
    turtle.circle(-20, 140)
    turtle.seth(-85)
    turtle.forward(18)
    turtle.pu()
    turtle.goto(50, 115)
    turtle.pd()
    turtle.goto(-50, 115)
    turtle.pu()
    turtle.end_fill()
    turtle.goto(19, 115)
    turtle.pd()
    turtle.goto(50, 115)
    turtle.seth(0)
    turtle.fillcolor('gold2')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.seth(90)
    turtle.circle(10, 90)
    turtle.seth(0)
    turtle.circle(10, 90)
    turtle.seth(270)
    turtle.circle(10, 90)
    turtle.seth(180)
    turtle.circle(10, 90)
    turtle.pu()
    turtle.end_fill()
    turtle.goto(-19, 115)
    turtle.pd()
    turtle.goto(-50, 115)
    turtle.seth(0)
    turtle.fillcolor('gold2')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.seth(90)
    turtle.circle(10, 90)
    turtle.seth(0)
    turtle.circle(10, 90)
    turtle.seth(270)
    turtle.circle(10, 90)
    turtle.seth(180)
    turtle.circle(10, 90)
    turtle.pu()
    turtle.end_fill()

def body():
    # 上半身
    turtle.goto(-25, 8)
    turtle.seth(240)
    turtle.pd()
    turtle.circle(150, 15)
    turtle.seth(270)
    turtle.circle(40, 15)
    turtle.circle(15, 65)
    turtle.seth(0)
    turtle.forward(10)
    turtle.circle(10, 100)
    turtle.seth(90)
    turtle.circle(10, 100)
    turtle.seth(180)
    turtle.forward(10)
    turtle.pu()
    turtle.goto(25, 8)
    turtle.seth(-60)
    turtle.pd()
    turtle.circle(-150, 15)
    turtle.seth(270)
    turtle.circle(-40, 15)
    turtle.circle(-15, 65)
    turtle.seth(180)
    turtle.forward(10)
    turtle.circle(-10, 100)
    turtle.seth(90)
    turtle.circle(-10, 100)
    turtle.seth(0)
    turtle.forward(10)
    turtle.pu()
    turtle.goto(-20, 4)
    turtle.pd()
    turtle.goto(-16, -4)
    turtle.goto(16, -4)
    turtle.goto(20, 4)
    turtle.pu()
    turtle.goto(0, -5)
    turtle.pd()
    turtle.goto(0, -50)
    turtle.pu()
    turtle.goto(-30, -48)
    turtle.pd()
    turtle.goto(-30, -60)
    turtle.pu()
    turtle.goto(30, -48)
    turtle.pd()
    turtle.goto(30, -60)
    turtle.pu()
    turtle.goto(-30, -55)
    turtle.pd()
    turtle.goto(30, -55)
    turtle.pu()
    turtle.goto(-30, -60)
    turtle.pd()
    # 参数 1 为绘制颜色，参数 2 为填充颜色
    turtle.color('black', 'red')
    turtle.begin_fill()
    turtle.goto(30, -60)
    turtle.pu()
    # 下半身
    turtle.goto(-25, -60)
    turtle.pd()
    turtle.goto(-35, -100)
    turtle.goto(-20, -100)
    turtle.goto(-0, -60)
    turtle.goto(20, -100)
    turtle.goto(35, -100)
    turtle.goto(25, -60)
    turtle.end_fill()
    turtle.pu()
    turtle.goto(-33, -100)
    turtle.pd()
    turtle.color('black', 'blue')
    turtle.begin_fill()
    turtle.seth(270)
    turtle.circle(6, 180)
    turtle.end_fill()
    turtle.pu()
    turtle.goto(33, -100)
    turtle.pd()
    turtle.color('black', 'blue')
    turtle.begin_fill()
    turtle.seth(270)
    turtle.circle(-6, 180)
    turtle.end_fill()
    turtle.pu()


def word():
    turtle.color('red')
    turtle.goto(-30, 150)
    turtle.pd()
    turtle.write('鼠', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-10, 150)
    turtle.pd()
    turtle.write('你', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(10, 150)
    turtle.pd()
    turtle.write('有', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(30, 150)
    turtle.pd()
    turtle.write('钱', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-30, -150)
    turtle.pd()
    turtle.write('鼠', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-10, -150)
    turtle.pd()
    turtle.write('你', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(10, -150)
    turtle.pd()
    turtle.write('健', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(30, -150)
    turtle.pd()
    turtle.write('康', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-90,-10)
    turtle.pd()
    turtle.write('鼠', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-90, -30)
    turtle.pd()
    turtle.write('你', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-90, -50)
    turtle.pd()
    turtle.write('快', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(-90, -70)
    turtle.pd()
    turtle.write('乐', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(90, -10)
    turtle.pd()
    turtle.write('鼠', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(90, -30)
    turtle.pd()
    turtle.write('你', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(90, -50)
    turtle.pd()
    turtle.write('幸', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.goto(90, -70)
    turtle.pd()
    turtle.write('运', move=False, align='center', font=('Arial', 14, 'normal'))
    turtle.pu()
    turtle.hideturtle()


if __name__ == '__main__':
    head()
    hat()
    body()
    word()
    # 隐藏画笔
    turtle.hideturtle()
    # 停止画笔，但不关闭窗体
    turtle.done()