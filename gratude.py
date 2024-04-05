import tkinter as tk
import random
from itertools import cycle

messages = [
    "Thank you for always being there.",
    "Your support during tough times means the world.",
    "You light up life in the darkest times.",
    "Your patience and understanding is truly amazing.",
    "I appreciate the countless hours you've spent on calls.",
    "You're not just a friend, you're a rock."
    
]

def show_random_message():
    message = random.choice(messages)
    
    label.config(text=message)

    root.after(2000, show_random_message) 

root = tk.Tk()
root.title("Gratitude App")

root.configure(bg='pink')

label = tk.Label(root, text="", width=50, height=10, bg='pink')
label.pack()

root.after(0, show_random_message)
root.mainloop()
