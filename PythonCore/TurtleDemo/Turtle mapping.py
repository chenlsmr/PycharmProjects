import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
        turtle.circle(rad, angle/2)
        turtle.fd(rad)
        turtle.circle(neckrad+1, 180)
        turtle.fd(rad/2*3)
def drakSnack_c(rad, len):
     turtle.seth(0)
     turtle.fd(rad)
     turtle.seth(120)
     turtle.fd(rad)
     turtle.seth(240)
     turtle.fd(rad)
     turtle.fd(50)
     turtle.circle(len*2)


def main():
     turtle.setup(0.85, 0.6, 0, 0)
     pythonsize = 1
     speed = 5
     turtle.speed(speed)
     turtle.pensize(pythonsize)
    # turtle.pencolor("red")
    # turtle.seth(-40)
    # drawSnake(40,80,5,pythonsize/2)
     getflower()

def text():
     turtle.write("hello world!", font=("Arial", 23, "bold"))
     time.sleep(2)

def getflower():
     turtle.bgpic("timg.gif")
     turtle.color("red", "yellow")
     turtle.begin_fill()
for i in range(50):
     turtle.fd(200)
     turtle.left(170)
     turtle.end_fill()
     time.sleep(2)

main()
