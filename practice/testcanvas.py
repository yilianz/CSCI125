import turtle
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()

t = turtle.RawTurtle(canvas)
for _ in range(5):
    t.forward(15)
    t.left(35)

def clear():
    print("inside")
    canvas.delete("all")


tk.Button(root, text="clear", command=clear).pack()

root.mainloop()