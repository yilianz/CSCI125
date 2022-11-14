import turtle

window = turtle.Screen()

'''

tess = turtle.Turtle()

tess.speed(0)

tess.color('purple', 'light blue')

tess.begin_fill()

while True:

    tess.forward(200)

    tess.left(170)

    if abs(tess.pos()) < 1:

        break

tess.end_fill()

window.mainloop()

'''

i = turtle.Turtle()

i.shape("turtle")

 

'''

i.speed(1)

i.begin_fill()

for _ in range(4):

    i.left(90)

    i.forward(90)

i.end_fill()

'''

s = 80

i.pensize(s)

 

flag=1

 

def big():

    global s

    s = s + 3

    i.pensize(s)

def smol():

    global s

    s = s - 3

    i.pensize(s)

 

def red():

    i.color("red")

def orange():

    i.color("orange")

def yellow():

    i.color("yellow")

def green():

    i.color("green")

def blue():

    i.color("blue")

def purple():

    i.color("purple")

def pink():

    i.color("pink")

def black():

    i.color("black")

def white():

    global flag

    flag=0

def erase():

    i.color("white")

def glow(x,y):

    i.fillcolor("red")

def unglow(x,y):

    i.fillcolor("")

 

i.onclick(glow)

i.onrelease(unglow)

 

def move(x,y):

    global flag

    if flag==1:

        i.pendown()

    else:

        i.penup()

        flag=1

    i.forward(0)

    i.goto(x,y)

 

window.onclick(move)

 

window.onkey(red,"1")

window.onkey(orange,"2")

window.onkey(yellow,"3")

window.onkey(green,"4")

window.onkey(blue,"5")

window.onkey(purple,"6")

window.onkey(pink,"7")

window.onkey(black,"8")

window.onkey(white,"9")

window.onkey(erase,"0")

window.onkey(big,"+")

window.onkey(smol,"-")

window.listen()

window.mainloop()