import tkinter
from tkinter import StringVar
from tkinter import PhotoImage

# main application window
app = tkinter.Tk()
app.title("image Demo")

# main frame
mainframe = tkinter.Frame(app, relief='raised', borderwidth=5)
mainframe.pack() 

##################### start  ##########################
# 
image1 = PhotoImage(file='scream.gif')
image2 = PhotoImage(file='smile.gif')
image3 = PhotoImage(file='surprise.gif')


## get the image label
imglabel = tkinter.Label(mainframe) ## get the label
imglabel['image']=image3
imglabel.pack(padx = 20, pady = 10)

## Action 
def displaysmile():
    imglabel['image']=image2

def displayscream():
    imglabel['image']=image1

## click button
original = tkinter.Button(mainframe,text="Smile", command=displaysmile)
different= tkinter.Button(mainframe,text="Scream", command=displayscream)

original.pack(padx=30, pady=10)
different.pack(padx=30, pady=10)



#####################  end  ###########################

# keep the window open
app.mainloop()