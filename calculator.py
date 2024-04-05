import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror('Error', str(e))

def clear():
    entry.delete(0, tk.END)

def toggle_theme():
    current_theme = root["background"]
    if current_theme == "white":
        root["background"] = "black"
        root["foreground"] = "white"
    else:
        root["background"] = "white"
        root["foreground"] = "black"

root = tk.Tk()
root.title("VANSHIKA'S CALCULATOR")
root["background"] = "white"

entry = tk.Entry(root, width=25, font=('Arial', 14), bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button_text in buttons:
    if button_text == "=":
        tk.Button(root, text=button_text, width=10, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button_text == "C":
        tk.Button(root, text=button_text, width=10, height=2, command=clear).grid(row=row, column=col, padx=5, pady=5)
    elif button_text == "dark mode / light mode":
        tk.Button(root, text=button_text, width=10, height=2, command=toggle_theme).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button_text, width=10, height=2, command=lambda x=button_text: entry.insert(tk.END, x)).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
