import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning('Warning', 'Please select a task to remove.')

def mark_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(index, bg=selected_color.get())
    except IndexError:
        messagebox.showwarning('Warning', 'Please select a task to mark as completed.')

def change_theme(theme):
    if theme == 'Light Mode':
        root.config(bg='white')
        frame_tasks.config(bg='white')
        listbox_tasks.config(bg='white', fg='black')
        scrollbar_tasks.config(bg='white', troughcolor='grey')
    elif theme == 'Dark Mode':
        root.config(bg='black')
        frame_tasks.config(bg='black')
        listbox_tasks.config(bg='black', fg='white')
        scrollbar_tasks.config(bg='black', troughcolor='white')

# Create the main window
root = tk.Tk()
root.title('To-Do List')

# Theme selection
selected_theme = tk.StringVar()
selected_theme.set('Light Mode')
theme_label = tk.Label(root, text='Select Theme:')
theme_label.pack()
theme_options = ['Light Mode', 'Dark Mode']
theme_menu = tk.OptionMenu(root, selected_theme, *theme_options, command=lambda theme: change_theme(theme))
theme_menu.pack()

# Color selection
selected_color = tk.StringVar()
selected_color.set('white')
color_label = tk.Label(root, text='Select Color:')
color_label.pack()
color_options = ['blue', 'red', 'pink', 'yellow', 'purple']
color_menu = tk.OptionMenu(root, selected_color, *color_options)
color_menu.pack()

# Create GUI elements
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, border=0)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text='Add Task', width=48, command=add_task)
button_add_task.pack(pady=5)

button_remove_task = tk.Button(root, text='Remove Task', width=48, command=remove_task)
button_remove_task.pack(pady=5)

button_mark_task = tk.Button(root, text='Mark Task as Completed', width=48, command=mark_task)
button_mark_task.pack(pady=5)

root.mainloop()
