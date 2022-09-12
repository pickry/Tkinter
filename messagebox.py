from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Messagebox')
win.geometry("400x400")

def showinfo():
    messagebox.showinfo('Important!','This might take a minute..')

def error():
    messagebox.showerror('Error','The specified path does not exist')

def que():
    messagebox.askquestion('Age','Are you 13 years old or above?')

def cancel():
    messagebox.askokcancel('Delete','Are you sure you want to delete?')

def yesno():
    messagebox.askyesno('Confirmation','Are you sure you want to proceed?')

def retry():
    r = messagebox.askretrycancel('Failure','Do you want to try again?')
    if r:
        print('Retry')
    else:
        print('Cancel')

def warn():
    messagebox.showwarning('WARNING','This might lead to malfunction of the app')

B1 = Button(win, text='Information', command=showinfo, bg='sky blue', fg='white', activebackground='light green')
B1.place(x=100, y=100)

B2 = Button(win, text='Error', command=error, bg='sky blue', fg='white', activebackground='light green')
B2.place(x=100, y=200)

B3 = Button(win, text='Retry', command=retry, bg='sky blue', fg='white', activebackground='light green')
B3.place(x=100, y=300)

B4 = Button(win, text='Question', command=que, bg='sky blue', fg='white', activebackground='light green')
B4.place(x=200, y=100)

B5 = Button(win, text='cancel', command=cancel, bg='sky blue', fg='white', activebackground='light green')
B5.place(x=200, y=200)

B6 = Button(win, text='Yes or No', command=yesno, bg='sky blue', fg='white', activebackground='light green')
B6.place(x=200, y=300)

B7 = Button(win, text='Warning', command=warn, bg='sky blue', fg='white', activebackground='light green')
B7.place(x=300, y=100)

win.mainloop()
