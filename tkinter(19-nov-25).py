
import tkinter as tk
from tkinter import messagebox
import mysql.connector



def signUp_page_details():

    def new_user_register():
        new_user = new_userName.get()
        new_password = new_userPassword.get()

        if new_user == '' or new_password == '':
            messagebox.showwarning('WARNING','please enter your details to create your acc....')
            return
        
        class db_exception(Exception):
            pass
        
        try:
            conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'shashadb25',
            database = 'tkinter_project',
            port = '3306',
            autocommit = False
            )

            cur = conn.cursor()

            if conn and conn.is_connected() == False:
                    raise db_exception('sql/db connection is failed')
        
        except db_exception as e:
            conn.rollback()
            tk.Label(frame, text=f'{e}', font=('Arial',8)).grid(row=7, column=0, pady=10)

        else:
            inserting_data = 'insert into checking_user_details(db_user_name,db_password) values(%s, %s);'
            cur.execute(inserting_data,(new_user,new_password))
            conn.commit()
            messagebox.showinfo('INFO','Created your Account Successfully:')
            tk.Label(frame, text='Now you can login your account through Login Page', font=('Arial',8)).grid(row=7, column=0, pady=10)

        finally:
            if conn and conn.is_connected():
                cur.close()
                conn.close()

    sign_up = tk.Tk()
    sign_up.title('SignUp Page')
    sign_up.geometry('800x800')

    frame = tk.Frame(sign_up, bd=2, height= 600, width=600, relief='solid')
    frame.pack(pady=150)

    tk.Label(frame, text='creating a New Account:', font=('Arial',32)).grid(row=0, column=0 ,pady=10)
    tk.Label(frame, text='Please enter your details:', font=('Arial',16)).grid(row=1, column=0, pady=10)

    tk.Label(frame, text='USERNAME:', font=('Arial',18)).grid(row=2, column=0,pady=20)
    new_userName = tk.Entry(frame, bd=1, relief='solid',width=15, font=('Arial',12))
    new_userName.grid(row=3, column=0 ,padx=0)

    tk.Label(frame, text='PASSWORD:', font=('Arial',18)).grid(row=4, column=0,pady=20)
    new_userPassword = tk.Entry(frame, bd=1, relief='solid',width=15, font=('Arial',12))
    new_userPassword.grid(row=5, column=0, padx=0)

    tk.Button(frame, text='Create Account', bd=1, height=1, width=15, relief='solid', command=new_user_register).grid(row=6, column=0, pady=20)


    sign_up.mainloop()
    
attempts = 3
def login_page_details():
    global attempts
    user_Name = user_name.get()
    user_Password = user_password.get()
    

    if user_Name == '' or user_Password == '':
        messagebox.showwarning('WARNING','please enter your details to login....')
        return
    
    class db_exception(Exception):
        pass

    try:
        conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'shashadb25',
        database = 'tkinter_project',
        port = '3306'
        )

        cur = conn.cursor()

        query = 'select * from checking_user_details where db_user_name = %s and db_password = %s;'
        cur.execute(query,(user_Name,user_Password))
        result = cur.fetchone()

        if conn and conn.is_connected() == False:
            raise db_exception('sql/db connection is failed')
        
    except db_exception as e:
        tk.Label(frame, text=f'{e}', font=('Arial',8)).grid(row=9, column=0, pady=10)
    
    else:
        
        if result:
            messagebox.showinfo('INFO','you have been logged in successfully.....')
        else:
            attempts -= 1
            messagebox.showerror('ERROR','login fail:check once your details')
            if attempts <= 0:
                tk.Label(frame, text=f'sorry..try again after 24 hours', font=('Arial',8)).grid(row=10, column=0, pady=10)
            else:
                tk.Label(frame, text=f'you have only {attempts} attempts left', font=('Arial',8)).grid(row=10, column=0, pady=10)

    finally:
        if conn and conn.is_connected():
            cur.close()
            conn.close()


root = tk.Tk()
root.title('Login Page')
root.geometry('1200x800')

frame = tk.Frame(root, bd=2, height= 600, width=600, relief='solid')
frame.pack(pady=150)

tk.Label(frame, text='Checking Your Details:', font=('Arial',32)).grid(row=0, column=0 ,pady=10)
tk.Label(frame, text='Please enter your login details:', font=('Arial',16)).grid(row=1, column=0, pady=10)

tk.Label(frame, text='USERNAME:', font=('Arial',18)).grid(row=2, column=0,pady=20)
user_name = tk.Entry(frame, bd=1, relief='solid',width=15, font=('Arial',12))
user_name.grid(row=3, column=0 ,padx=0)

tk.Label(frame, text='PASSWORD:', font=('Arial',18)).grid(row=4, column=0,pady=20)
user_password = tk.Entry(frame, show="*", bd=1, relief='solid',width=15, font=('Arial',12))
user_password.grid(row=5, column=0, padx=0)

tk.Label(frame, text=f"don't have an account click on sign up button", font=('Arial',8)).grid(row=6, column=0, pady=10)

tk.Button(frame, text='SUBMIT', bd=1, height=1, width=8, relief='solid', command=login_page_details).grid(row=7, column=0, pady=10)
tk.Button(frame, text='SIGN UP', bd=1, height=1, width=8, relief='solid', command=signUp_page_details).grid(row=8, column=0,pady=10)

root.mainloop()


