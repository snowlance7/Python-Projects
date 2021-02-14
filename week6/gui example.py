import sys
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Blackjack")
root.geometry("300x200")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

button1 = ttk.Button(frame, text="Click me!")
button1.pack()

root.mainloop()