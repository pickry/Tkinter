'''Tcl tk
1. Tcl is a dynamic interpreted programming language
2. Tk is a tcl package. Adds custom commands
3. themed tk a new family of tk widgets

MODULES
1. ttk 
2. colorchooser
3. commondialog
4. filedialog
5. simpledialog
6. font
7. messagebox
8. turtle'''

# import tkinter 
# from tkinter import ttk
# import tkinter.colorchooser

# win = tkinter.Tk()
# win.title('Tkinter color chooser')

# def changecolor():
#     colors = tkinter.colorchooser.askcolor()
#     win.configure(bg=colors[1])

# ttk.Button(win,text='Pick Color',command=changecolor).pack()
# win.mainloop()

#georgia = tkFont.Font(family='georgia',size=30,weight='bold')


import tkinter as ttk
from tkinter import messagebox

def dialog():
    messagebox.showerror('answer','Sorry no ans available')
ttk.Button(text='Answer',command=dialog).pack()
ttk.mainloop()

