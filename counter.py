'''
1. button
2. motion
3. buttonrelease
4. enter
5. leave
6. focusin
7. focusout
8. return
9. key
10. configure
'''
from tkinter import *

win = Tk()
win.title('Event Handling!')

def motion(event):
    print(f'Current position of cursor is ({event.x}, {event.y})...')
    return

c = Canvas(win, bg='pink',width=500, height=400)
c.bind('<Motion>', motion)
c.pack()
win.mainloop()