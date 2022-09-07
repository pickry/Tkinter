from tkinter import *

win = Tk()
win.title('Canvas!')

canvas = Canvas(win, width=500, height=500, bg='sky blue', cursor='dotbox')
canvas.pack()

canvas.create_arc(5,10,100,100)
canvas.create_line(0,80,500,80)
canvas.create_oval(200,200,400,400)
canvas.create_text(250,10, text='Using Canvas')
canvas.create_bitmap(210,50,bitmap='questhead')
points = [100,100,120,100,140,120,120,140,100,140,80,120]
canvas.create_polygon(points, fill='pink')
win.mainloop()