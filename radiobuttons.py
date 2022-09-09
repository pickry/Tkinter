from tkinter import *

win = Tk()
win.title("Radio Buttons!")

def pri():
    wind = Tk()
    c = Canvas(wind, bg='light green')
    c.pack()
    c.create_text(100,10, text='value accepted!', fill='purple', font=16)
    wind.mainloop()

v = IntVar()
Radiobutton(win, text='RadioButton 1', variable=v, activebackground='pink',activeforeground='purple',command=pri).grid(row=0)

v2 = IntVar()
Radiobutton(win, text='RadioButton 2', variable=v2, activebackground='pink',activeforeground='purple',command=pri).grid(row=1)

var1 = IntVar()
Checkbutton(win, text='Check Button 1',variable=var1).grid(row=3)

var2 = IntVar()
Checkbutton(win, text='Check Button 2', variable=var2).grid(row=4)

win.mainloop()

