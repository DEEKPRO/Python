from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Window set up
root = Tk()
root.title("Denomination Calculator Launcher")
root.geometry("1000x650")
root.configure(bg="slategrey")

#Image&Intro
image = Image.open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson6\image.png")
ima = ImageTk.PhotoImage(image)
lab = Label(master=root,image=ima, bg="cornflowerblue")
tex = Label(master=root, text="Welcome to Denomination Launcher")
tex.pack()
lab.pack(padx=250,pady=10)
def ask():
    askuser = messagebox.showinfo("Denomination Setup", "Do you want to launch denomination calculator?")
    if askuser == "ok":
        topwin()
asking = Button(master=root, command=ask, text="Launch Denomination Calculator")
asking.pack()



#Denomination Calculator
def topwin():
    window = Toplevel()
    window.title("Denomination Calculator")
    window.geometry("500x500")
    window.configure(bg="cornflowerblue")
    text = Label(master=window, text="Enter your number below👇")
    ent = Entry(master=window)
    t1 = Entry(master=window, state="normal")
    t2 = Entry(master=window, state="normal")
    t3 = Entry(master=window, state="normal")
    
    #Calculator
    def calculator():
        num = int(ent.get())
        no2000 = 0
        while num > 2000:
            no2000 += 1
            num -= 2000
        no500 = 0
        while num > 500:
            no500 += 1
            num -= 500
        no100 = 0
        while num > 100:
            no100 += 1
            num -= 100
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)

        t1.insert(END, str(no2000))
        t2.insert(END, str(no500))
        t3.insert(END, str(no100))
    but = Button(master=window, text="Calculate", command=calculator)
    text.pack()
    ent.pack()
    but.pack()
    t1.pack()
    t2.pack()
    t3.pack()
root.mainloop()