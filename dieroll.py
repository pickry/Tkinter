import random
from tkinter import *

win = Tk()
win.title('Dice')

def picknumber():
    label["text"] = str(random.randint(1,6))

button = Button(win, width=20, bg='light yellow', fg='blue', command= picknumber, bd=3, relief=SUNKEN, activebackground='white', text='ROLL')
button.pack()

label = Label(win, width=20, bg='sky blue', fg='purple')
label.pack()

win.mainloop()