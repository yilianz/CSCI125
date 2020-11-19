import turtle
import random

wn = turtle.Screen()
police = turtle.Turtle()   #police
me =  turtle.Turtle()      #player
#wn.addshape('mario.gif')
police.shape("turtle")

######################### start ###################
###Action -- Automatic
def go():
    step = random.randint(4,7)*10
    direction = random.randint(1,36)*10
    police.forward(step)
    police.left(direction)
    wn.ontimer(go,2000)

##Bind to timer
wn.ontimer(go,2000)  # 1000 -- 1 second


########################### end #################
wn.listen()
wn.mainloop()