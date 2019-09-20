from tkinter import *
from tkinter import messagebox
import tkinter.ttk
import tkinter
import sqlite3
import datetime
from PIL import ImageTk, Image
import os
def add():
    maintk.destroy()
    import add
def edit():
    maintk.destroy()
    import edit
maintk = Tk()
maintk.title("Gestió DAC")
Label(maintk, text="Gestió DAC Farmacia Laura Pons", font=("Arial Bold", 40)).pack()
Button(maintk,text="Afegir medicamet i pacient",command=add).pack()
Button(maintk,text="Buscar i veure pacients amb medicaments",command=edit).pack()
maintk.mainloop()