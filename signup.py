from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confrimpasswordEntry.delete(0,END)

def connect_mysqldb():
    if emailEntry.get=='' or userEntry.get()=='' or passwordEntry.get =='' or confrimpasswordEntry.get =='':
        messagebox.showerror('Error','All fields are required')
    elif passwordEntry.get() != confrimpasswordEntry.get():
        messagebox.showerror('Error', 'Password mismatch')
    else:
        try:
            con= pymysql.connect(host='localhost',user='root',password='12345')
            mycursor= con.cursor()
        except:
            messagebox.showerror('database Connectivity issue,try again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            query='create table data1(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='insert into data1(email,username,password)values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),userEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Sucess','Registration is sucessful')
        clear()
    signup_window.destroy()
    import signin





def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.resizable(0,0)
signup_window.title('signup page')

bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=bgImage)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)


heading=Label(frame,text='CREATE A NEW ACCOUNT',font=('Microsoft Yahel UI Light',16,'bold'),bg='white'
,fg='firebrick')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahel UI Light',13),bg='white'
,fg='firebrick')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=25,font=('Microsoft Yahel UI Light',13)
                 ,fg='white',bg='firebrick')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


userLabel=Label(frame,text='Username',font=('Microsoft Yahel UI Light',13),bg='white'
,fg='firebrick')
userLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

userEntry=Entry(frame,width=25,font=('Microsoft Yahel UI Light',13)
                 ,fg='white',bg='firebrick')
userEntry.grid(row=4,column=0,sticky='w',padx=25)



passwordLabel=Label(frame,text='Password',font=('Microsoft Yahel UI Light',13),bg='white'
,fg='firebrick')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahel UI Light',13)
                 ,fg='white',bg='firebrick')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)




confrimpasswordLabel=Label(frame,text='Confrim Password',font=('Microsoft Yahel UI Light',13),bg='white'
,fg='firebrick')
confrimpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confrimpasswordEntry=Entry(frame,width=25,font=('Microsoft Yahel UI Light',13)
                 ,fg='white',bg='firebrick')
confrimpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

signupbutton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick',fg='white',activebackground='firebrick',activeforeground='white',
                    command=connect_mysqldb)
signupbutton.grid(row=10,column=0,pady=(20,0))

alreadyaccount=Label(frame,text='Already had an account!',font=('Open Saans',11),
                   fg='firebrick',bg='white',activeforeground='firebrick',activebackground='white',cursor='hand2',bd=0)
alreadyaccount.grid(row=11,column=0,padx=25,sticky='w',pady=(10,0))



newaccountButton=Button(signup_window,text='Login',font=('Open Saans',9,'bold','underline'),
                   fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=login_page)
newaccountButton.place(x=750,y=449)


signup_window.mainloop()