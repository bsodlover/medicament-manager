#FIXME: make buttons useful
#FIXME:ºfer q el cliejnt no se inseti ni el medicamen ts no estab bens posats 
from tkinter import *
import tkinter
import sqlite3
import datetime
from tkinter import messagebox
tk = Tk()
namR = []
data = []
rowNum = 2 #we define the row to start creating the grids
db_data = []
clientDetailsEntry = []
clientDetailsText = []
clientDetailsValue = []
top_frame = tkinter.Frame(tk).grid(row=0, column=0)
#some global variables 
columnNum=0
i = 0
iii = 0
now = datetime.datetime.now()
errors = 0
def add_product():
    global clientDetailsText
    global errors
    conn = sqlite3.connect('db.db')
    params = (clientDetailsValue[0],clientDetailsValue[1],clientDetailsValue[2],clientDetailsValue[3],clientDetailsValue[4])
    conn.execute("INSERT INTO patient (pName,pNum,pLocation,pFamily,pDoctor) VALUES (?,?,?,?,?)",params)
    conn.commit()
    for ii in data:
        global i
        global db_data 
        i = i + 1
        if not ii.get():
            messagebox.showerror("Error","Falta informació de un medicament")
            errors = 1
        db_data.append(ii)
        if i == 6 and errors == 0: #we store rows in the database, we select 4 items, which are the colmns of the rows
            params = (1,clientDetailsValue[0],now.strftime("%Y-%m-%d"),db_data[0].get(),db_data[1].get(),db_data[2].get(),db_data[3].get(),db_data[4].get(),db_data[5].get())
            conn.execute("INSERT INTO medicaments (mState,mPatientName,mDate,mName,mDosi,mPauta,mDataInici,mDataFinal,mObservacions) VALUES (?,?,?,?,?,?,?,?,?)", params);
            conn.commit()
            #we clear this variables to start the loop again
            db_data = []
            i = 0
    conn.close() 
    messagebox.showinfo('Informació', 'Els medicaments i el pacient han sigut emmagatzemats correctament.')
    
def create_row():
    global rowNum
    global columnNum
    global namR
    global data
    columnNum=0 # we set columnnum to 0 to start creating rows from the left
    for ii in range(0,6): #we make a loop to create rows
        namR.append(Entry(top_frame))
        namR[ii].grid(row=rowNum, column=columnNum)
        columnNum = columnNum + 1
    rowNum = rowNum + 1
    for e in namR:
        data.append(e)
    namR = [] 

def destroy_row():
    for ii in range(0,6):
        entry = data.pop(-1)
        entry.destroy()

def prepare_grid():
    global top_frame
    btnText = ["Afegir medicament","Treure medicament","Extra","TEST"]
    labelText = ["Nom medicament","Dosi","Pauta","Data inici","Data final","Observacions"]
    tkinter.Button(top_frame, text = btnText[0], fg = "green", command = create_row).grid(row=0, column=0)
    tkinter.Button(top_frame, text = btnText[1], fg = "green", command = destroy_row).grid(row=0, column=1)
    tkinter.Button(top_frame, text = btnText[2], fg = "green", command = create_row).grid(row=0, column=2)
    tkinter.Button(top_frame, text = btnText[3], fg = "green", command = add_product).grid(row=0, column=3)
    for ii in range(0,6):
        Label(top_frame, width=20, height=4, bg="green", text=labelText[ii]).grid(row=2, column=ii)
    create_row() #we create a row to start with an empty row

def popup():
    global i 
    global top_frame
    global clientDetailsText
    global iii
    global rowNum
    def checkpatient():
        global errors
        for ii in clientDetailsEntry:
            if not ii.get():
                errors = 1
        if errors == 1:
            messagebox.showerror("Error","Falten dades del pacient")
            errors = 0
        else:
            for ii in clientDetailsEntry:
                clientDetailsValue.append(ii.get())
            popup.destroy()
            prepare_grid()
    #Name Section
    popup = Toplevel()
    clientDetailsText =  ["Nom","Telf.","Adreça","Familiar","Doctor"]
    for ii in clientDetailsText:
        Label(popup, bg="green", width=10, height=4, text = ii).grid(row=0, column=i)
        clientDetailsEntry.append(Entry(popup, width=10))
        clientDetailsEntry[i].grid(row=1, column=i)
        i = i + 1
    rowNum = rowNum + 1
    i = 0
    Button(popup,command=checkpatient, fg="green",text="Guardar").grid(row=2,column=2)
popup()
tk.mainloop()