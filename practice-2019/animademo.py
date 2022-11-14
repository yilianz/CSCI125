import turtle
import random

wn = turtle.Screen()
police = turtle.Turtle()   #police
me =  turtle.Turtle()      #player
#wn.addshape('mario.gif')
police.shape("turtle")
me.speed(2)
######################### start ###################
###Action -- Automatic
def go():
    step = random.randint(4,7)*10
    direction = random.randint(1,36)*10
    police.forward(step)
    police.left(direction)
    wn.ontimer(go,2000)   # set a timer
def move(x,y):
    me.goto(x,y)
##Bind to timer
wn.ontimer(go,2000)  # 1000 -- 1 second  for police after 2 second, the police will go
wn.onclick(move)  # for player

########################### end #################
wn.listen()
wn.mainloop()