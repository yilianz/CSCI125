import tkinter
from tkinter import StringVar

winapp = tkinter.Tk()
winapp.title("Find movies")

#### start ###########
mainframe = tkinter.Frame(winapp)
mainframe.pack()

name = StringVar()
output = StringVar()
tkinter.Label(mainframe, text="Please Enter the movie").pack()
tkinter.Entry(mainframe, textvariable=name).pack()
tkinter.Label(mainframe,textvariable = output).pack()

def findmovie():
    ## input 
    n = name.get()
    f = open("topmovies.txt",'r')
    print(n)
    output.set("Not Found")
    for line in f:
        if line.find(n) != -1:
            output.set("Found the Movie: "+ line)
    f.close()

tkinter.Button(mainframe,text="Click to find",command=findmovie).pack()

#### end  #####
winapp.mainloop()
