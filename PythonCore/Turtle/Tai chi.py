import turtle as tl
#绘制“阴阳”的函数
def yinyang(radius,filling_color,inside_color):
    #对画笔进行必要的初始化
    tl.pensize(3)
    tl.shape("circle")
    tl.color('black',filling_color)

    #设置填充着色标记
    tl.begin_fill()
    #绘制处于外围的“太阴”或者“太阳”
    tl.circle(radius/2,180)
    tl.circle(radius,180)
    tl.left(180)
    tl.circle(-radius/2,180)
    #填充颜色并关闭标记
    tl.end_fill()

    #画笔转移
    tl.left(90)
    tl.penup()
    tl.forward(radius*0.35)
    tl.right(90)

    # 绘制处于内部的“少阴”或者“少阳”
    tl.pendown()
    tl.color(filling_color,inside_color)
    #设置填充着色标记
    tl.begin_fill()
    tl.circle(radius*0.15)
    #填充颜色并关闭标记
    tl.end_fill()