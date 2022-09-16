from tkinter import *

win = Tk()
win.title('Event Handling!')

def pressedkey(event):
    print(event.char)

win.bind("<Key>", pressedkey)

win.mainloop()