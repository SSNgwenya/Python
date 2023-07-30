import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    meters_input = entry_int.get()
    km_output = meters_input * 0.001 
    output_string.set(km_output)

# window
window = ttk.Window(themename = 'darkly')
window.title('My Demo')
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = 'Meters to Kilometers', font = 'Calibri 24 bold')
title_label.pack()


# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)


# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = ' Calibre 24', textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()
