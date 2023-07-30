import tkinter as tk
from tkinter import ttk

def beast():
    # get the content of the entry
    #print(entry.get())
    entry_text = entry.get()
    
    
    # update label
   # label['text'] = "Sunny becomes a coder"
    label.config(text = entry_text)
    
# window
window = tk.Tk()
window.title('Sunny is Sexy AF!')

# widgets

# Label
label = ttk.Label(master = window, text = 'King', font = 'Calibre 12 bold')
label.pack()


# entry
entry = ttk.Entry(master = window)
entry.pack()


#button
button = ttk.Button(master = window, text = 'Enter', command = beast)
button.pack()


# run
window.mainloop()
