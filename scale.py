from tkinter import *

win = Tk()
win.title('Scroll')

scale = Scale(win, from_=0, to=100, bg='light yellow',fg='black',orient='horizontal',label='SCALE WIDGET',troughcolor='white')
scale.pack()

spinbox = Spinbox(win, from_=0, to=10, bg='light grey',fg='orange',font='Arial 12 italic')
spinbox.pack()

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=Y)

list = Listbox(win, yscrollcommand=scrollbar.set, font='Georgia 20',bg='sky blue',width=40)

for i in range(51):
    list.insert(END, str(i)+ '. We are checking the list and scrollbar together')

list.pack(side=RIGHT, fill=Y, expand=True)

scrollbar.config(command=list.yview)
win.mainloop()