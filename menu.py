from tkinter import *

win = Tk()
win.title("Menu")

menu = Menu(win)
win.config(menu=menu)

tool = Menu(menu, bg='gray', fg='black', activebackground='sky blue')
menu.add_cascade(label='Tool', menu=tool)

tool.add_command(label='Pen')
tool.add_command(label='Brush')
tool.add_command(label='Pencil')
tool.add_command(label='Eraser', command=win.quit)

size = Menu(menu)
menu.add_cascade(label='Size', menu=size)

size.add_command(label='1px')
size.add_command(label='3px')
size.add_command(label='4px')
size.add_command(label='6px')

colors = Menu(menu, activebackground='light green', bg='light yellow')
menu.add_cascade(label='Colors', menu=colors)

colors.add_command(label='red')
colors.add_command(label='yellow')
colors.add_command(label='blue')
win.mainloop()