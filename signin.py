from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
#Funtionality Part


def forgot_pass():
    def change_pass():
        if usernameEntry.get()=='' or newpasswordEntry.get()=='' or confrimpasswordEntry.get()=='':
            messagebox.showerror('error','All fields are required',parent=window)
        elif newpasswordEntry.get()!=confrimpasswordEntry.get():
            messagebox.showerror('error', 'Password mismatch', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='12345',database='userdata')
            mycursor = con.cursor()
            query='select * from data1 where username=%s'
            mycursor.execute(query,(usernameEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('error', 'Wrong username', parent=window)
            else:
                query='update data1 set password=%s where username=%s'
                mycursor.execute(query,(newpasswordEntry.get(),usernameEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('sucess', 'Reset password sucessfull', parent=window)
                window.destroy()





    window=Toplevel()
    window.title('change password')

    bgImage = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window, image=bgImage)
    bgLabel.grid()

    heading = Label(window, text='REST PASSWORD', font=('Microsoft Yahel UI Light', 20, 'bold'), bg='white'
                    , fg='firebrick')
    heading.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('Microsoft Yahel UI Light', 13), bg='white'
                      , fg='firebrick')
    userLabel.place(x=470,y=130)

    usernameEntry=Entry(window,width=25,font=('Microsoft Yahel UI Light',13)
                 ,fg='white',bg='firebrick')
    usernameEntry.place(x=470, y=160)



    newpasswordLabel = Label(window, text='New password', font=('Microsoft Yahel UI Light', 13), bg='white'
                      , fg='firebrick')
    newpasswordLabel.place(x=470, y=210)

    newpasswordEntry = Entry(window, width=25, font=('Microsoft Yahel UI Light', 13)
                          , fg='white', bg='firebrick')
    newpasswordEntry.place(x=470, y=240)



    confrimpasswordLabel = Label(window, text='Confrim password', font=('Microsoft Yahel UI Light', 13), bg='white'
                             , fg='firebrick')
    confrimpasswordLabel.place(x=470, y=290)

    confrimpasswordEntry = Entry(window, width=25, font=('Microsoft Yahel UI Light', 13)
                             , fg='white', bg='firebrick')
    confrimpasswordEntry.place(x=470, y=320)

    submitbutton = Button(window, text='Submit', font=('Open Sans', 16, 'bold'), bd=0, bg='firebrick', fg='white',
                          activebackground='firebrick', activeforeground='white',
                          command=change_pass)
    submitbutton.place(x=470,y=390)



    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('error','All fields are required')
    else:
        try:
            con= pymysql.connect(host='localhost',user='root',password='12345')
            mycursor= con.cursor()
        except:
            messagebox.showerror('database Connectivity issue,try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data1 where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('error','Invaild username or password')
        else:
            messagebox.showinfo('Sucess','login is sucessful')



def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUI part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('loginpage')

bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahel UI Light',23,'bold'),bg='white'
,fg='firebrick')
heading.place(x=600,y=110)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahel UI Light',11,'bold'),bd=0,fg='firebrick')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
frame1=Frame(login_window,width=250,height=2,bg='firebrick')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahel UI Light',11,'bold'),bd=0,fg='firebrick')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)


forgetButton=Button(login_window,text='Forgot password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahel UI Light',9,'bold'),fg='firebrick',activeforeground='firebrick',command=forgot_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',font=('Open Saans',16,'bold'),
                   fg='white',bg='firebrick',activeforeground='white',activebackground='firebrick',cursor='hand2',width=19,bd=0,command=login_user)
loginButton.place(x=578,y=350)

orLabel=Label(login_window,text='--------------OR----------------',font=('Open Sans',16),fg='firebrick',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
facebookLabel=Label(login_window,image=facebook_logo,bg='white')
facebookLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create a new account',font=('Open Saans',7,'bold','underline'),
                   fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)



login_window.mainloop()