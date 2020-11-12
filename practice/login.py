#
# python app --- Let user enter a keycode and then check whether the keycode is valid
#  if yes, You are logged in,   if no, ask the user to retry it 

import tkinter

## Window and Titlefor the application ##
app = tkinter.Tk()
app.title("Login Window")

## Frame to put in the window 
mainframe = tkinter.Frame(app,background="pink")
mainframe.pack()

###### start to put widget in the mainframe  ####################
entercode = tkinter.Entry(mainframe, width = 20)
entercode.pack(padx=10, pady=10)

#Action -- check the keycode
def checkcode():
    # take the input
    usercode = entercode.get()
    # open the file ***
    f = open('keycode.txt','r')

    # read the file line by line and check whether it is the same as usercode
    for line in f:
        if line[:-1] == usercode:
            print(f'{usercode} is valid') # put the message in the gui 
            break
    
    f.close()
    

# button
clickbutton = tkinter.Button(mainframe,text="check", command=checkcode)
clickbutton.pack(padx=20, pady= 10)


### Ending--- keep the window open ##
app.mainloop()