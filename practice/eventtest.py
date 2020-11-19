import turtle

wn = turtle.Screen()  #windows
I = turtle.Turtle()   # turtle

########  start  ######################
I.pensize(20)
## event handler
def move(x,y):
    I.goto(x,y)
def gored():
    I.color("red")
def goleft():
    I.left(90)
    I.forward(100)

## event
wn.onclick(move)  # whenever you click, move the mouse to the position
wn.onkey(gored,"r")  # press r --- call function gored  
#practice change to green
wn.onkey(goleft,"Left")  # case sensitve


#########  end  ########################
wn.listen()
wn.mainloop()