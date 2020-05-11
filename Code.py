import turtle
import mouse
import random

back = "back.png"
but = "button.gif"

win = turtle.Screen()
win.addshape(but)
win.tracer(0)
win.bgpic(back)

button9 = turtle.Turtle()
button9.shape(but)
button9.showturtle()
button9.pu()
button9.goto(61,-122)
win.update()

while True:
    if mouse.is_pressed():
        dx = random.randint(-10,10)
        dy = random.randint(-10,10)
        x = button9.xcor()
        y = button9.ycor()
        button9.goto(x+dx,y+dy)
    win.update()
