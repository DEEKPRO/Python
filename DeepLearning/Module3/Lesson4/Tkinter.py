from tkinter import *
window = Tk()
window.title("Tkinter Practice")
window.geometry("300x300")

lab = Label(text="Hello", fg='black', bg='white')
but = Button(text="Click me", bg="black", fg="white")
ent = Entry(fg="yellow", bg="blue", width=50)
lab.pack()
but.pack()
ent.pack()

fra = Frame(master=window,relief=SUNKEN, borderwidth=10, bg="green")
fra.pack()
label = Label(master=fra, text="This is inside a frame.", fg="black")
label.pack()
text = Text(master=fra, fg="cornflowerblue")
text.pack()
window.mainloop()