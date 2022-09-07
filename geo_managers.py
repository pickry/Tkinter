from tkinter import *

win = Tk()
win.title("Geometry Managers!")



'''PACK'''
# frame1 = Frame(win, width=200, height=100, bg='orange')
# frame1.pack(fill=BOTH, side=LEFT,expand=True)

# frame2 = Frame(win, width=100, bg='purple')
# frame2.pack(fill=BOTH, side=LEFT,expand=True)



'''PLACE'''
# frame = Frame(win, width=150, height=150)
# frame.pack()

# button1 = Button(frame, text="Button at (10,20)", bg='pink')
# button1.place(x=10,y=20)

# button2 = Button(frame, text="Button at (40,50)",bg='yellow')
# button2.place(x=40,y=50)



'''GRID'''
for i in range(3):
    win.columnconfigure(i, weight=1, minsize=75)
    win.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = Frame(win,relief=SUNKEN)
        frame.grid(row=i, column=j, padx=5,pady=5)
        Button1 = Button(frame, text=f'Row{i}\nColumn{j}')
        Button1.pack(padx=5,pady=5)


win.mainloop()

