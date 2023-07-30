import tkinter as tk
from tkinter import ttk
#import ttkbootstrap as ttk


def button_fun():
    print('Button was pressed')

def hello():
    print('Hello')
        
    
# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a Test')
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise: creating text label and a button with a function to print 'hello' and the label should say "my label" between the entry widget and the button
text_exercise = tk.Label(master = window, text = 'My Label')
text_exercise.pack()

b_exercise = ttk.Button(master = window, text = 'My Button', command = hello)
b_exercise.pack()


#ttk button
button = ttk.Button(master = window, text = 'Button', command = button_fun)
button.pack()


# run
window.mainloop()
