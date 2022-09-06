from tkinter import *

win = Tk()
win.title("Frames")

frame = Frame(win)
frame.pack(side=LEFT)

frame2 = Frame(win)
frame2.pack(side=RIGHT)

b1 = Button(frame, text='Button1',bg='pink',fg='white')
b1.pack()

b2 = Button(frame, text='Button2', bg='Sky blue',fg='white')
b2.pack()

b3 = Button(frame2, text = 'Button3',bg='purple',fg='white')
b3.pack()

b4 = Button(frame2,text='Button4',bg='light green',fg='white')
b4.pack()

win.mainloop()

