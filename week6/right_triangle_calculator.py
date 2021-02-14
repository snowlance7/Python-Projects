import sys
import tkinter as tk
from tkinter import ttk
import math

def btnCalculateClicked():
    side_a = int(sideAText.get())
    side_b = int(sideBText.get())

    side_c = math.sqrt((side_a ** 2) + (side_b ** 2))

    sideCText.set(str(round(side_c,3)))

def btnExitClicked():
    root.destroy()

#Window Construction
root = tk.Tk()
root.title("Right Triangle Calculator")
root.geometry("300x200")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

sideAText = tk.StringVar()
sideBText = tk.StringVar()
sideCText = tk.StringVar()

lblSideA = ttk.Label(frame, text="Side A:").grid(column=0, row=0, sticky=tk.E)
txtSideA = ttk.Entry(frame, textvariable=sideAText).grid(column=1, row=0)

lblSideB = ttk.Label(frame, text="Side B:").grid(column=0, row=1, sticky=tk.E)
txtSideB = ttk.Entry(frame, textvariable=sideBText).grid(column=1, row=1)

lblSideC = ttk.Label(frame, text="Side C:").grid(column=0, row=2, sticky=tk.E)
lblSideC = ttk.Label(frame, textvariable=sideCText).grid(column=1, row=2)

btnCalculate = ttk.Button(frame, text="Calculate", command=btnCalculateClicked).grid(column=0, row=3)
btnExit = ttk.Button(frame, text="Exit", command=btnExitClicked).grid(column=1, row=3)


root.mainloop()