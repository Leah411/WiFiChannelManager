import tkinter as tk
import os
global main_screen

login_screen = None

#register screen
def register():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry


    username = tk.StringVar()
    password = tk.StringVar()



    register_screen = tk.Toplevel(main_screen)
    register_screen.geometry("800x800")
    register_screen.configure(bg="black")
    register_screen.title("register")

    tk.Label(register_screen, text=" enter details below:", bg="black",fg="white",font=15).pack()
    tk.Label(register_screen,text="",bg="black").pack()
    tk.Label(register_screen,text="",bg="black").pack()
    username_label = tk.Label(register_screen,text="Username ",bg="black",fg="blue",font="Arial")
    username_label.pack()
    username_entry= tk.Entry(register_screen, textvariable=username)
    password_entry = tk.Entry(register_screen, textvariable=password, show='*')
    username_entry.pack()
    password_label = tk.Label(register_screen,text="Password ",bg="black",fg="blue",font="Arial")
    password_label.pack()
    password_label= tk.Entry(register_screen, textvariable=password,show='*')
    password_label.pack()
    tk.Label(register_screen,text="",bg="black").pack()
    tk.Button(register_screen,text="Register",width=10,height=1,bg="blue",fg="white",command=register_user).pack()
    print("error1")


#login screen
def login():
    global username_login_entry
    global password_login_entry
    global username_verify
    global password_verify, login_screen


    login_screen = tk.Toplevel(main_screen)
    login_screen.geometry("800x800")
    login_screen.configure(bg="black")
    login_screen.title("login")

    tk.Label(login_screen, text=" enter details below:", bg="black",fg="white",font=15).pack()
    tk.Label(login_screen,text="",bg="black").pack()
    tk.Label(login_screen,text="",bg="black").pack()


    username_verify=tk.StringVar()
    password_verify=tk.StringVar()


    tk.Label(login_screen, text="Username * ",bg="black",fg="blue",font="Arial").pack()
    username_login_entry = tk.Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    tk.Label(login_screen, text="",bg="black").pack()
    tk.Label(login_screen, text="Password * ",bg="black",fg="blue",font="Arial").pack()
    password_login_entry = tk.Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    tk.Label(login_screen, text="",bg="black").pack()
    tk.Button(login_screen, text="Login", width=10,height=1,bg="blue",fg="white", command=login_verification).pack()

    print("error2")




#Implementing event on register buttom
def register_user():
    username_info = username.get()
    password_info = password.get()
    print("done")
    with open("file.txt","a") as f:
        f.write(username_info+"\n")
        f.write(password_info+"\n")
    print("error3")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    tk.Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

#implementing event on register button

def login_verification():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)
    print(f"{username1=}, {password1=}")
    with open('file.txt') as myfile:
        data = myfile.read()
        if username1 in data:
            if password1 in data:
                login_sucess()
            else:
                password_not_recognized()
        else:
            user_not_found()

#popup for login screen
def login_sucess():
    global login_success_screen
    login_success_screen = tk.Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    tk.Label(login_success_screen, text="Login Success").pack()
    tk.Button(login_success_screen, text="OK", command=delete_login_success).pack()


#popup for login invalid password
def password_not_recognized():
    global password_not_recog_screen
    password_not_recog_screen = tk.Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    tk.Label(password_not_recog_screen, text="Invalid Password ").pack()
    tk.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

#popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = tk.Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    tk.Label(user_not_found_screen, text="User Not Found").pack()
    tk.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()






#main screen

main_screen= tk.Tk()
main_screen.geometry("400x400")
main_screen.configure(bg="black")
main_screen.title("Account Login")
#
#create a Form labal

label = tk.Label(
    text="choose Login Or Register",
    fg="blue",
    bg="black",
    font="Arial",
    width="300",
    height="2"

)
label.pack()


# create Login Button
loginMe = tk.Button(
    text="to log in, click here",
    width=25,
    height=5,
    bg="black",
    fg="blue",
    font=15,
    command=login
)
loginMe.pack()



# # create register Button
registerMe = tk.Button(
    text="to sign up, click here",
    width=25,
    height=5,
    bg="black",
    fg="blue",
    font=15,
    command=register
)
registerMe.pack()
print("error5")

main_screen.mainloop()  # start the GUI
