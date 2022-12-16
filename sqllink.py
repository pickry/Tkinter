from tkinter import *
import sqlite3
'''pip install sqlite3'''
import tkinter.messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
root.config(background="#ffe6f0")


fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()
var_c1= "Java" 
var_c2 = "Python" 
var_c3 = 'C++'
radio_var=StringVar() 
def database():
   first=fn.get() 
   second=ln.get() 
   dob1=dob.get()
   var1=var.get() 
   var3=var_c1
   var3=var_c2
   var3=var_c3
   var4=radio_var.get() 
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (FName TEXT,LName TEXT,DOB DATE,Country TEXT,ProgLanguage TEXT,Gender Text)')
   cursor.execute('INSERT INTO Student (FName, LName, DOB, Country, ProgLanguage, Gender) VALUES(?,?,?,?,?,?)',(first,second,dob1,var1,var3,var4))
   conn.commit()
   tkinter.messagebox.showinfo('Congratulations!!', 'The user has successfully signed up!')
    
    
heading = Label(root, text='Registration Form', relief=SOLID, width=20, font='arial 19 bold', fg='#b30047', bg='#ffe6f0')
heading.place(x=90, y=10)
fname = Label(root, text="FirstName :",width=20,font=("bold", 10),bg='#ffe6f0')
fname.place(x=80,y=70)
efname = Entry(root,textvar=fn)
efname.place(x=240,y=70)
lname = Label(root, text="LastName :",width=20,font=("bold", 10),bg='#ffe6f0')
lname.place(x=80,y=120)
elname = Entry(root,textvar=ln)
elname.place(x=240,y=120)
date = Label(root, text="DOB :",width=20,font=("bold", 10),bg='#ffe6f0')
date.place(x=80,y=170)
edob = Entry(root,textvar=dob)
edob.place(x=240,y=170)

Country = Label(root, text="Country :",width=20,font=("bold", 10),bg='#ffe6f0')
Country.place(x=75,y=220)
List=["Nepal","India",'America','China',"Canada",'Japan','South Africa']
droplist=OptionMenu(root,var,*List)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=238,y=220)
Lang = Label(root, text="Prog Language :",width=20,font=("bold", 10),bg='#ffe6f0')
Lang.place(x=95,y=270)
c1 = Checkbutton(root, text="java", variable=var_c1).place(x=235,y=270)  
c2 = Checkbutton(root, text="python", variable=var_c2).place(x=290,y=270)  
c3 = Checkbutton(root, text='C++', variable=var_c3).place(x =350, y=270)
Gender = Label(root, text="Gender :",width=20,font=("bold", 10),bg='#ffe6f0')
Gender.place(x=73,y=320)
r1=Radiobutton(root, text="Male", variable=radio_var, value="Male").place(x=230,y=320)  
r2=Radiobutton(root, text="Female", variable=radio_var, value="Female").place(x=290,y=320) 
Submit=Button(root, text='Submit',width=12,bg='#ff4d94',fg='white',command=database).place(x=130,y=400)
quit=Button(root, text='Quit',width=12,bg='#ff4d94',fg='white',command=exit).place(x=280,y=400)
root.mainloop()
