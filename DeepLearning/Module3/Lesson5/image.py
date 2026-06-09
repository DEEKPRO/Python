from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("1000x1000")
window.title("Image")
ima = Image.open("C:\Deekshith\DeekPython\Python\DeepLearning\Module3\Lesson5\images.jpg")
image = ImageTk.PhotoImage(ima)
lab = Label(master=window, image=image, height=500, width=400)
label = Label(master=window, text="This is below an image.")
lab.pack()
label.pack()
window.mainloop()