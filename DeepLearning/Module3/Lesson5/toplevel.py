from tkinter import *

window = Tk()
window.title("Root Window")
window.geometry("1000x1000")
lab = Label(master=window, text="Root window")
lab.pack()

def toplevel():
    top = Toplevel()
    top.title("Top Level")
    top.geometry("500x500")
    label = Label(master=top, text="Top window")
    label.pack()
    top.mainloop()

but = Button(master=window, text="Top level activator", command=toplevel)
but.pack()
window.mainloop()