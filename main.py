from tkinter import*
root =Tk()
root.title('Login page')
root.geometry("650x550")
L1 =Label(text='Login Page', underline=90)
L1.pack()



def login_clicked():
    print("Login button clicked!")


username_label = Label(root,text="Username:")
username_label.pack(pady=10)  # Add padding

username_entry = Entry(root, width=40)
username_entry.pack()

F_name_label = Label(root,text="Father name:")
F_name_label.pack(pady=10)  # Add padding

F_name_entry = Entry(root, width=50)
F_name_entry.pack()

email_label = Label(root, text="Email:")
email_label.pack(pady=10)

email_entry = Entry(root, width=50)
email_entry.pack()
password_label = Label(root, text="Password:")
password_label.pack(pady=10)

password_entry = Entry(root, width=20, show="*")
password_entry.pack()

login_button = Button(root, text="Login", command=login_clicked)
login_button.pack(pady=15)





root.mainloop()
