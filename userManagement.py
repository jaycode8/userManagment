from tkinter import *
from validate_email import validate_email
from tkinter.messagebox import *
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '4174',
    database = 'pydb'
)
mycursor = mydb.cursor()

def handleSubmit(userName, email, mobile, gender, passw, window):
    if userName == '' or email == '' or mobile == '' or gender == '' or passw == '':
        showwarning('user management system', 'All fields are required !')
    else:
        is_valid = validate_email(email)
        if is_valid == True:
            sql = "INSERT INTO Users VALUES (%s, %s, %s, %s, %s)"
            data = (userName, email, mobile, gender, passw)
            mycursor.execute(sql, data)
            mydb.commit()
            res = showinfo('user management system', 'User successfully regesters')
            if res == 'ok':
                window.destroy()
        else:
            showwarning('user management system', 'Invalid email address')

def handleLog(user_name, password):
    if user_name == '' or password == '':
        showwarning('user management system', 'All fields are required !')
    else:
        query = 'SELECT * FROM Users WHERE userName = %s AND password=%s'
        values = (user_name, password)
        mycursor.execute(query, values)
        myreslt = mycursor.fetchall()
        if myreslt == []:
            showerror('user management system', 'Details mismatch or dont have account.')
        else:
            for i in myreslt:
                name = i[0]
            showinfo('user management system', 'welcome '+ name)

def regForm(ws):
    ws.destroy()
    window = Tk()
    window.title('Regestration')

    f = ('Mali', 14)
    var = StringVar()
    var.set('male')

    right_frame = Frame(window, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

    Label(right_frame, text="Enter Name", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)
    Label(right_frame, text="Contact Number", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)
    Label(right_frame, text="Select Gender", bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter Password", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)

    gender_frame = LabelFrame(right_frame, bg='#CCCCCC', padx=10, pady=10,)
    register_name = Entry(right_frame, font=f)
    register_email = Entry(right_frame, font=f)
    register_mobile = Entry(right_frame, font=f)

    male_rb = Radiobutton(gender_frame, text='Male', bg='#CCCCCC', variable=var, value='male',font=('Times', 10),)
    female_rb = Radiobutton(gender_frame, text='Female', bg='#CCCCCC', variable=var, value='female',font=('Times', 10),)
    register_pwd = Entry(right_frame, font=f,show='*')

    register_btn = Button(right_frame, text='Submit', width=10 ,font=f, relief=SOLID, cursor='hand2', command=lambda : handleSubmit(register_name.get(), register_email.get(), register_mobile.get(), var.get(), register_pwd.get(), window))
    log_btn = Button(right_frame, text='Have Account', width=10, font=f, relief=SOLID, cursor='hand2', command=lambda : logPage(window))

    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    log_btn.grid(row=7, column=0, pady=10)
    register_btn.grid(row=7, column=1, pady=10)
    right_frame.pack()

    gender_frame.grid(row=3, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=LEFT)
    female_rb.pack(expand=True, side=LEFT)


    window.mainloop()

def logPage(window):
    if(window == ''):
        pass
    else:
        window.destroy()
    ws = Tk()
    ws.title('Log In')

    f = ('Mali', 14)

    right_frame = Frame(ws, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

    Label(right_frame, text="User Name", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)
    Label(right_frame, text="Password", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)

    user_name = Entry(right_frame, font=f)
    password = Entry(right_frame, font=f, show='*')

    sign_in = Button(right_frame, text='Log in', width=10 ,font=f, relief=SOLID, cursor='hand2', command=lambda : handleLog(user_name.get(),password.get()))
    sign_up = Button(right_frame, text='New', width=10, font=f, relief=SOLID, cursor='hand2', command=lambda : regForm(ws))

    user_name.grid(row=0, column=1, pady=10, padx=20)
    password.grid(row=1, column=1, pady=10, padx=20)
    sign_in.grid(row=7, column=1, pady=10)
    sign_up.grid(row=7, column=0, pady=10)
    right_frame.pack()

    ws.mainloop()

if __name__ == '__main__':
    logPage('')
