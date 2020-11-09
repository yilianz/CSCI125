import turtle

wn = turtle.Screen()
wn.addshape("mario.gif")

class mario(turtle.Turtle):
    #initialize
    def __init__(self,shape,color):
        super().__init__(shape)      # parent initilization
        self.color(color)
    # new methods for child 
    def left(self):
        self.seth(180)
        self.forward(50)
    def right(self):
        self.seth(0)
        self.forward(50)

I = mario("mario.gif","yellow")
He = mario("turtle","red")

wn.onkey(I.left,"Left")
wn.onkey(He.left,"a")
wn.listen()
wn.mainloop()    
