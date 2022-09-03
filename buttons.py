import tkinter

win = tkinter.Tk()
win.title('Button!')

button = tkinter.Button(win, text='Quit',command=win.destroy, width=7, height=4,
 activebackground='pink',activeforeground='purple'
,bg='Sky blue', fg='white', font='Georgia', relief='ridge')
'''
justify
padx
pady
state
underline
wraplength
'''
button.pack()
win.mainloop()