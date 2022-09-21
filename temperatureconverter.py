from tkinter import *

win = Tk()
win.title("Temperature Converter")

def fahrenheittocelsius():
    f = temp1.get()
    c = (5/9) * (float(f)-32)
    temp2["text"] = f'{round(c,2)}\N{DEGREE CELSIUS}'
frame = Frame(win)
frame.grid(row=0, column=0, padx=10)

temp1 = Entry(frame, width=10)
temp1.grid(row=0, column=0)

f = Label(frame, text="\N{DEGREE FAHRENHEIT}")
f.grid(row=0, column=1)

button = Button(win, text="\N{RIGHTWARDS BLACK ARROW}", command= fahrenheittocelsius, bg='sky blue')
button.grid(row=0, column=1, pady=10)

temp2 = Label(win, text='\N{DEGREE CELSIUS}')
temp2.grid(row=0, column=2, padx=10)

win.mainloop()