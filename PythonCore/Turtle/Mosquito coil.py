import turtle as t
import time
R = 150
t.speed(100)
t.pensize(3)
t.color("blue")

for i in range(50):
    t.circle(R - i * 3, 180)