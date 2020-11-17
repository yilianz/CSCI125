import tkinter
from tkinter import StringVar

# main application window
app = tkinter.Tk()
app.title("BMI calculator")

# main frame
mainframe = tkinter.Frame(app, relief='raised', borderwidth=5, background="blue")
mainframe.pack() 

##################### start  ##########################
# get the input text box
weightbox = tkinter.Entry(mainframe, width = 40)
weightbox.insert(0,"Enter the weight")
weightbox.pack(padx= 20, pady= 20)

heightbox = tkinter.Entry(mainframe, width = 40)
heightbox.insert(0, "Enter the height")
heightbox.pack(padx= 20, pady= 20)

## Action --- Calculate BMI
ans = StringVar()     # a holder which hold the string value
def bmi():
    w = float(weightbox.get())
    h = float(heightbox.get())

    ans.set(str(703*w/(h**2)))


# Get the button
calculatebutton = tkinter.Button(mainframe,text="Calculate BMI", command=bmi)
calculatebutton.pack(padx = 20, pady = 20)

## get the output label --- inside
bmilabel = tkinter.Label(mainframe, textvariable=ans) ## get the label
bmilabel.pack(padx = 20, pady = 10)
#####################  end  ###########################

# keep the window open
app.mainloop()