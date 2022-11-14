import tkinter
from tkinter import StringVar

# main application window
app = tkinter.Tk()
app.title("Radio Button Demo")

# main frame
mainframe = tkinter.Frame(app, relief='raised', borderwidth=5)
mainframe.pack() 

##################### start  ##########################
# 
phone = StringVar()
home = tkinter.Radiobutton(mainframe, text='Home',variable=phone,value="803-443-1234")
office = tkinter.Radiobutton(mainframe, text='Office',variable=phone,value="803-443-2222")
cell = tkinter.Radiobutton(mainframe, text='Mobile',variable=phone,value="803-443-5555")



home.pack(padx=30, pady=10)
office.pack(padx=30, pady=10)
cell.pack(padx=30, pady=10)

## get the output label --- inside
bmilabel = tkinter.Label(mainframe, textvariable=phone) ## get the label
bmilabel.pack(padx = 20, pady = 10)
#####################  end  ###########################

# keep the window open
app.mainloop()