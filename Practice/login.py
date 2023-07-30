import tkinter as tk
from tkinter import messagebox


# making a window
window = tk.Tk()
window.title("Loging Form")
window.geometry('340x440')
window.configure(bg="#333333")

frame = tk.Frame(bg='#333333')

def info():
    messagebox.showinfo('Thank you')

# Creating Widgets

login_label = tk.Label(frame, text = 'Login', bg="#333333", fg='#FF3399', font='Arial 30')
username_label = tk.Label(frame, text = 'Username', bg="#333333", fg='#FFFFFF', font = "Arial 16")
username_entry = tk.Entry(frame, font = "Arial 16")
password_entry = tk.Entry(frame, show = "*", font = "Arial 16")
password_label = tk.Label(frame, text = "Password", bg="#333333", fg='#FFFFFF',font = "Arial 16")
login_button = tk.Button(frame, text = "Login", bg="#FF3399", font = "Arial 16", command = info)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady = 20)


frame.pack()

window.mainloop()