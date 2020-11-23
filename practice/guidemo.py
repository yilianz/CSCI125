import tkinter
from tkinter import StringVar

# main application window
app = tkinter.Tk()
app.title("Determine your letter grade")

# main frame
mainframe = tkinter.Frame(app, relief='raised', borderwidth=5, background="blue")
mainframe.pack() 

##################### start  ##########################
#Textbox
thelabel = tkinter.Label(mainframe, text="please enter your grade")
thelabel.pack()

gradeBox = tkinter.Entry(mainframe, width=40)
gradeBox.pack(padx=10,pady=20)

##Action
ans=StringVar()
def checkgrade():
    yourgrade= int(gradeBox.get())
    if yourgrade >=90:
        print(yourgrade)
        ans.set("A")
    elif yourgrade >=80:
        ans.set("B")
# Get the button
clickbutton = tkinter.Button(mainframe,text="check", command=checkgrade)
clickbutton.pack(padx = 20, pady = 20)

## get the output label --- inside
mylabel = tkinter.Label(mainframe, textvariable=ans) ## get the label
mylabel.pack(padx = 20, pady = 10)
#####################  end  ###########################
# keep the window open
app.mainloop()
