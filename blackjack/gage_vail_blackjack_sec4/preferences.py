import sys
import tkinter as tk
from tkinter import ttk

class Preference():
    def __init__(self):
        self.name = str()
        self.language = str()
        self.auto_save = int()
    
    def getFromFile(self):
        try:
            with open("preferences.txt") as f:
                self.name = f.readline().rstrip("\n")
                self.language = f.readline().rstrip("\n")
                self.auto_save = int(f.readline().rstrip("\n"))
        except:
            self.name = ""
            self.language = "English"
            self.auto_save = 5
        
    
    def writeToFile(self):
        with open("preferences.txt","w") as f:
            f.write(self.name + "\n")
            f.write(self.language + "\n")
            f.write(str(self.auto_save) + "\n")

# Window Construction
root = tk.Tk()
root.title("Right Triangle Calculator")
root.geometry("400x200")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

nameText = tk.StringVar()
languageText = tk.StringVar()
autoSaveText = tk.StringVar()
nameMsg = tk.StringVar()
languageMsg = tk.StringVar()
autoSaveMsg = tk.StringVar()

def btnSaveClicked():
    cont = True
    pref = Preference()

    if nameText.get() == "":
        nameMsg.set("Required.")
        cont = False
    else:
        nameMsg.set("")

    if languageText.get() == "":
        languageMsg.set("Required.")
        cont = False
    else:
        languageMsg.set("")
    
    try:
        pref.auto_save = int(autoSaveText.get())
        autoSaveMsg.set("")
    except:
        autoSaveMsg.set("Must be valid integer.")
        cont = False

    if cont:
        pref.name = nameText.get()
        pref.language = languageText.get()
        pref.writeToFile()
        root.destroy()

def btnCancelClicked():
    root.destroy()


lblName = ttk.Label(frame,text="Name: ").grid(column=0,row=0,sticky=tk.E)
lblLanguage = ttk.Label(frame,text="Language: ").grid(column=0,row=1,sticky=tk.E)
lblAutoSave = ttk.Label(frame,text="Auto Save Every X Minutes: ").grid(column=0,row=2,sticky=tk.E)
txtName = ttk.Entry(frame,textvariable=nameText).grid(column=1,row=0)
txtLanguage = ttk.Entry(frame,textvariable=languageText).grid(column=1,row=1)
txtAutoSave = ttk.Entry(frame,textvariable=autoSaveText).grid(column=1,row=2)
lblNameMsg = ttk.Label(frame,text="",textvariable=nameMsg).grid(column=2,row=0)
lblLanguageMsg = ttk.Label(frame,text="",textvariable=languageMsg).grid(column=2,row=1)
lblAutoSaveMsg = ttk.Label(frame,text="",textvariable=autoSaveMsg).grid(column=2,row=2)
btnSave = ttk.Button(frame, text="Save", command=btnSaveClicked).grid(column=0, row=3)
btnCancel = ttk.Button(frame, text="Cancel", command=btnCancelClicked).grid(column=1, row=3)

pref = Preference()
pref.getFromFile()
nameText.set(pref.name)
languageText.set(pref.language)
autoSaveText.set(str(pref.auto_save))

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3) 

root.mainloop()

#Startup Code

