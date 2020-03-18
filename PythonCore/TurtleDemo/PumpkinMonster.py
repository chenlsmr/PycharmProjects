#  -*- coding: utf-8 -*- 
#  @Author   : 王翔 
#  @WeChat   : King_Uranus 
#  @公众号    : 清风Python 
#  @GitHub   : https://github.com/BreezePython 
#  @Date     : 2019/10/29 22:30 
#  @Software : PyCharm 
#  @version  ：Python 3.8.1 
#  @File     : PumpkinMonster.py 


import turtle as t 

def init():  16      #  初始化 
 17    t.bgpic('dark_night.png') 
 18    t.screensize(500, 500, bg='white') 
 19    t.speed(10) 
 20    t.hideturtle() 
 21    t.bgcolor('black') 
 22    t.bgpic('dark_night.png') 
 23 
 24 
 25def outline():  26      #   绘制南瓜轮廓 
 27    t.color('#CF5E1A', '#CF5E1A') 
 28    t.penup() 
 29    t.goto(250, 30) 
 30    t.pendown() 
 31    t.seth(90) 
 32    t.begin_fill() 
 33     for j in range(25):  34        t.fd(j) 
 35        t.left(3.6) 
 36     for j in range(25, 0, -1):  37        t.fd(j) 
 38        t.left(3.6) 
 39    t.seth(-90) 
 40    t.circle(254, 180) 
 41    t.end_fill() 
 42 
 43 
 44def tail():  45      #  绘制南瓜枝 
 46    t.penup() 
 47    t.goto(0, 180) 
 48    t.pendown() 
 49    t.color('#2E3C01') 
 50    t.seth(100) 
 51    t.pensize(25) 
 52    t.circle(60, 100) 
 53 
 54 
 55def eyes(args):  56      #  眼睛 
 57     for items in args:  58        position, angle, direction = items 
 59        t.pensize(6) 
 60        t.penup() 
 61        t.goto(position, 0) 
 62        t.pendown() 
 63        t.color('#4C180D', '#4C180D') 
 64        t.begin_fill() 
 65        t.seth(angle) 
 66         for j in range(55):  67            t.fd(3) 
 68             if direction:  69                t.left(3)    #  左转3度 
 70             else:  71                t.right(3)    #  左转3度 
 72        t.goto(position, 0) 
 73        t.end_fill() 
 74 
 75 
 76def nose():  77      #  鼻子 
 78    t.penup() 
 79    t.goto(0, 0) 
 80    t.seth(180) 
 81    t.pendown() 
 82    t.begin_fill() 
 83    t.circle(50, steps=3) 
 84    t.end_fill() 
 85 
 86 
 87def mouth():  88      #  嘴巴 
 89    t.color('#F9D503', '#F9D503') 
 90    t.pensize(6) 
 91    t.penup() 
 92    t.penup() 
 93    t.goto(-150, -100) 
 94    t.pendown() 
 95    t.begin_fill() 
 96    t.seth(-30) 
 97    t.fd(100) 
 98    t.left(90) 
 99    t.fd(30) 
100    t.right(90) 
101    t.fd(60) 
102    t.left(60) 
103    t.fd(60) 
104    t.right(90) 
105    t.fd(30) 
106    t.left(90) 
107    t.fd(100) 
108    t.end_fill() 
109    t.done() 
110 
111 
112if __name__ == '__main__': 113    init() 
114    outline() 
115    tail() 
    eyes_items = [(-60, 230, 0), (60, -50, 1)] 
    eyes(eyes_items) 
    nose() 
    mouth() 
    t.done() 
