import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.pensize(4)
t.pen(fillcolor="green",pencolor="blue")

t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(135)
t.forward(70)
t.left(90)
t.forward(70)

t.end_fill()
import time
time.sleep(10)
