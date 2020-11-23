import turtle
import random
wn = turtle.Screen()      # windows
wn.addshape('mario.gif')
police = turtle.Turtle()   #police
me =  turtle.Turtle()      #player
me.shape("mario.gif")
police.shape("turtle")
police.penup()
######################### start ###################

# event handler
def running():
    # do sth here
    step = random.randint(-7,7)*10   # 30 40 50 60 70
    police.forward(step)
    police.speed(4)   # please adjust the number
    wn.ontimer(running,500)
def goLeft():
    me.forward(20)
# bind the timer with the function
wn.ontimer(running, 500)   # move once
wn.onkey(goLeft,"Left")
###########################end ####################
wn.listen()
wn.mainloop()