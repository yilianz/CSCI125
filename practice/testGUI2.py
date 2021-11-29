import tkinter
from tkinter import StringVar

winapp = tkinter.Tk()
winapp.title("test demo")

frame = tkinter.Frame(winapp,background="#60FCF3")
frame.grid()
#frame.pack(padx=5, pady=6)

code = StringVar()
entercode = tkinter.Entry(frame, width = 20,textvariable=code)
#entercode.pack(padx=10, pady=10)
entercode.grid(row=0,column=0,padx=5,pady=30)

valid = StringVar()
result = tkinter.Label(frame,textvariable=valid,background="#60FCF3", width=20)
result.grid(row=0,column=2,padx=5,pady=30)
#result.pack()

def getvalue():
    usercode = code.get()
    print(usercode)
    f = open('keycodes.txt','r')
    valid.set("invalid code")

    # read the file line by line and check whether it is the same as usercode
    for line in f:
        if line[:-1] == usercode:
            #print(f'{usercode} is valid') # put the message in the gui 
            valid.set(usercode+" is valid")
            break
    
    f.close()

    


clickbutton = tkinter.Button(frame, text="Click", command=getvalue)
clickbutton.grid(row=1,column=1)
#clickbutton.pack()



winapp.mainloop()
