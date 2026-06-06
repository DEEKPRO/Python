import tkinter as tk
from Rpassword import generatepassword

def generate():
    try:
        val = generatepassword(int(len.get()))
        out.delete(0, tk.END)
        out.insert(0, val)
    except ValueError:
        print("How did you mess up the simplest program🤣?")

window = tk.Tk()
window.title("Password Generator")

len = tk.Entry(window, width=5)
len.insert(0, "16")
len.pack()

tk.Button(master=window, text="Generate", command=generate).pack()

out = tk.Entry(master=window, width=25)
out.pack()

window.mainloop()
