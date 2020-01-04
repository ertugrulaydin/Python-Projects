import turtle
t=turtle
t=turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.pen(pencolor="orange")
t.speed(2)
t.begin_fill()
t.right(45)
t.forward(70)
t.left(90)
t.forward(70)
t.left(135)
t.forward(100)
for i in range(0,3):
    t.left(90)
    t.forward(100)

t.end_fill()
import time
time.sleep(15)
