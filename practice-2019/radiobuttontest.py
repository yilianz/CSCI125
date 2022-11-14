import tkinter
from tkinter import StringVar

app = tkinter.Tk()    # windows
app.title("my radio buttons")  # title 
mainframe = tkinter.Frame(app, borderwidth=5)  # frame
mainframe.pack()

################ Start #############################
phone = StringVar()
home = tkinter.Radiobutton(mainframe,text="Home",variable=phone,value="803-443-1111")
office = tkinter.Radiobutton(mainframe,text="office",variable=phone, value="803-443-2222")


home.pack(padx=30, pady=10)
office.pack(padx=30, pady = 10)

phonelabel = tkinter.Label(mainframe, textvariable = phone)
phonelabel.pack(padx=30, pady = 10)


############### end ################################
app.mainloop()  # do not close