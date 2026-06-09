from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x100")
window.title("Virus Detector")

def warning():
    warn = messagebox.showwarning("Virus Detected", "Virus Detected")
    return warn

but = Button(master=window, command=warning, text="Exit")
lab = Label(master=window, text="This is a virus detector. Press the button below to exit.")
lab.pack()
but.pack()

window.mainloop()