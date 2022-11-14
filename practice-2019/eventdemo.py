import turtle

wn = turtle.Screen()   # window

me = turtle.Turtle()   # create a turtle with a name me
################  start  #####################
s = 20    # this is the global variable ---all functions can use S
me.pensize(s)
## Event Handler
def move(x,y):
    global s
    s = s + 10
    me.pensize(s)
    me.goto(x,y)
def red():
    global s
    s = s -10
    me.color("red")
def goLeft():
    me.left(90)
    me.forward(100)
## Event -- Click the mouse --- move to the position
wn.onclick(move)
wn.onkey(red,"r")    # click r  change the color to red
wn.onkey(goLeft,"Left") # corresponding to left arrow

#################  end  ##################
wn.listen()   # listen to the key event
wn.mainloop()







