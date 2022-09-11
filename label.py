from tkinter import *

win = Tk()
win.title("Display Text!")

my_message = Message(win, text='Hello Everyone, kindly pay attention! We are learning Tkinter', bg='pink', 
aspect=500, bd=5, relief=RIDGE, padx=10, fg='dark blue', font='Inkfree 14 italic')

label = Label(win, text='Label widget does not allow multiple lines!', bd=8, bg='sky blue',
cursor='cross', fg='yellow',font='Georgia 18 italic', relief=RAISED, height=2)

label.pack()
my_message.pack()

win.mainloop()