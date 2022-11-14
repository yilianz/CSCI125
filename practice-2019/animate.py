import turtle
import random

wn = turtle.Screen()
mario= wn.addshape('mario.gif')
me = turtle.Turtle()
me.shape("turtle")
me.speed(1)
me.penup()
police = turtle.Turtle()
police.shape('mario.gif')
police.penup()
police.speed(2)
# action
def doit():
    size = random.randint(1,10)*10
    degree = random.randint(1,360)
    police.forward(size)
    police.left(degree)

    wn.ontimer(doit,100)
def move(x,y):
    me.goto(x,y)

#binding
wn.ontimer(doit, 2000)
wn.onclick(move)
#listen
wn.listen()

#keep going
wn.mainloop()