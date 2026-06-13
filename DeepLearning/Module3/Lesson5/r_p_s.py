import random
from tkinter import *
from tkinter import messagebox

def compchoice(user):
    choice = random.randint(1,3)
    if user == choice:
        tie = messagebox.showinfo("RPS", "Computer picked the same!\n                Tie!")
    elif user - choice == 1:
        win = messagebox.showinfo("RPS", "You Win!")
    elif choice - user == 1:
        los = messagebox.showinfo("RPS", "Computer Wins!")
    elif user - choice == 2:
        los = messagebox.showinfo("RPS", "Computer Wins!")
    elif choice - user == 2:
        win = messagebox.showinfo("RPS", "You Win!")
    else:
        err = messagebox.showerror("Error", "There was an error!")

def rockfunc():
    compchoice(1)
def paperfunc():
    compchoice(2)
def scissfunc():
    compchoice(3)

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("700x500")
window.configure(bg="slategrey")
intro = Label(text="This is the famous game of Rock, Paper, Scissors. Please pick an option: ",font=("Google", 12))
rock = Button(text="🪨", width=15,height=2, command=rockfunc,font=("Arial", 12))
paper = Button(text="📃", width=15,height=2, command=paperfunc,font=("Arial", 12))
scissors = Button(text="✂️", width=15,height=2, command=scissfunc,font=("Arial", 12))
intro.pack()
rock.pack(pady=30)
paper.pack(pady=50)
scissors.pack(pady=70)


window.mainloop()