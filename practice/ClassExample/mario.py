import turtle
from time import sleep

wn = turtle.Screen()
wn.addshape("rightframe1.gif")
wn.addshape("rightframe2.gif")
wn.addshape("rightframe3.gif")
wn.addshape("leftframe1.gif")
wn.addshape("leftframe2.gif")
wn.addshape("leftframe3.gif")

class mario(turtle.Turtle):
    #initialize
    def __init__(self,shape,color):
        super().__init__(shape)      # parent initilization
        self.color(color)
        self.penup()
        self.speed(1)
    # new methods for child 
    def right(self):
        self.seth(0)
        for i in range(25):
            sleep(0.1)
            self.forward(3)
            if i%3 ==0:
                self.shape("rightframe1.gif")
            elif i%3==1:
                self.shape("rightframe2.gif")
            else:
                self.shape("rightframe3.gif")


        
#build the object

I = mario("rightframe1.gif","yellow")


wn.onkey(I.left,"Left")
wn.onkey(I.right,"Right")

wn.listen()
wn.mainloop()    
