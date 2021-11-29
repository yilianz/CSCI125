import tkinter
import random
from tkinter import StringVar
from tkinter import PhotoImage

# main application window
app = tkinter.Tk()
app.title("image Demo")

# main frame
mainframe = tkinter.Frame(app, relief='raised', borderwidth=5,height=300, width=450)
mainframe.pack() 

##################### start  ##########################
# 
image1 = PhotoImage(file='scream.gif')
image2 = PhotoImage(file='smile.gif')
image3 = PhotoImage(file='surprise.gif')


## get the image label
imglabel = tkinter.Label(mainframe,height=250,width=400) ## get the label
imglabel['image']=image3
imglabel.pack(padx = 20, pady = 10)
inputnumber = StringVar()
tkinter.Entry(mainframe,textvariable=inputnumber).pack()

## Action 
def displaysmile():
    imglabel['image']=image2

def displayscream():
    imglabel['image']=image1

def guessnumber():
    num = random.randint(1,3)
    if num == int(inputnumber.get()):
        print("You Win")
        displaysmile()
    else: 
        print(f'{num}  {inputnumber.get()} different')
        displayscream()


## click button
original = tkinter.Button(mainframe,text="Smile", command=displaysmile)
different= tkinter.Button(mainframe,text="Scream", command=displayscream)
tkinter.Button(mainframe,text="Guess Number from 1 to 3 ", command=guessnumber).pack()

original.pack(padx=30, pady=10)
different.pack(padx=30, pady=10)



#####################  end  ###########################

# keep the window open
app.mainloop()