import tkinter
from tkinter import StringVar

winapp = tkinter.Tk()
winapp.title("test demo")

frame = tkinter.Frame(winapp,background="#60FCF3")
frame.pack(padx=5, pady=6)

code = StringVar()
entercode = tkinter.Entry(frame, width = 20,textvariable=code)
entercode.pack(padx=10, pady=10)

valid = StringVar()
result = tkinter.Label(frame,textvariable=valid,background="#60FCF3")
result.pack()

def getvalue():
    usercode = code.get()
    valid.set(usercode)


clickbutton = tkinter.Button(frame, text="Click", command=getvalue)
clickbutton.pack()



winapp.mainloop()
