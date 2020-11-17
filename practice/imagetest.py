import tkinter
from tkinter import PhotoImage, StringVar

app = tkinter.Tk()    # windows
app.title("image")  # title 
mainframe = tkinter.Frame(app, borderwidth=5)  # frame
mainframe.pack()

################ Start #############################
image1 = PhotoImage(file="scream.gif")
image2 = PhotoImage(file="smile.gif")
image3 = PhotoImage(file="surprise.gif")
imagelist = [image1, image2, image3] # imagelist[0], imagelist[1],

# Display it in label
imglabel = tkinter.Label(mainframe)
imglabel['image']=image1
imglabel.pack(padx=20, pady = 10)

# Action -- display the corresponding image
def goSmile():
    imglabel['image']=image2
def goSurprise():
    imglabel['image']=image3

# click button
smilebutton = tkinter.Button(mainframe, text="smile",command=goSmile)
smilebutton.pack()
suprisebutton = tkinter.Button(mainframe, text="surprise",command=goSurprise)
suprisebutton.pack()

############### end ################################
app.mainloop()  # do not close