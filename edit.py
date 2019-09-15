from tkinter import *
import tkinter
import sqlite3
import datetime
from tkinter import messagebox
client = "nom"
tk = Tk()
namR = []
data = []
rowNum = 2 #we define the row to start creating the grids
db_data = []
select_data = []
checkbox_id = []
checkbox = []
temp_data = []
#some global variables 
columnNum=0
i = 0
now = datetime.datetime.now()
currentRow = ""
def create_row():
    global rowNum
    global columnNum
    global namR
    global data
    columnNum=0 # we set columnnum to 0 to start creating rows from the left
    for ii in range(0,6): #we make a loop to create rows
        namR.append(Entry(tk))
        namR[ii].grid(row=rowNum, column=columnNum)
        columnNum = columnNum + 1
    rowNum = rowNum + 1
    for e in namR:
        data.append(e)
        temp_data.append(e)
    namR = [] 

def get_rows():
    global namR
    global rowNum
    global i 
    i = 0
    conn = sqlite3.connect('db.db')
    print("Opened database successfully");
    params = (client,)
    cursor = conn.execute("SELECT * FROM medicaments where mPatientName = ? ",params)
    for row in cursor:
        checkbox_id.append(row[0])
        dataRow = [row[9],row[8],row[7],row[6],row[5],row[4]]
        print(dataRow)
        select_data.append(dataRow)
        create_row()
        for ii in dataRow:
            print(i)
            tempItem = temp_data.pop(-1)
            tempItem.insert(0,ii)
            i = i + 1
            if i == 6:
                i = 0
    conn.close()
            
def destroy_row():
    for ii in range(0,4):
        entry = data.pop(-1)
        entry.destroy()

top_frame = tkinter.Frame(tk).grid(row=0, column=0)
btnText = ["Afegir medicament","Treure medicament","Extra","TEST"]
labelText = ["Nom medicament","Dosi","Pauta","Data inici","Data final","Observacions"]
tkinter.Button(top_frame, text = btnText[0], fg = "green", command = create_row).grid(row=0, column=0)
tkinter.Button(top_frame, text = btnText[1], fg = "green", command = destroy_row).grid(row=0, column=1)
tkinter.Button(top_frame, text = btnText[2], fg = "green", command = create_row).grid(row=0, column=2)
tkinter.Button(top_frame, text = btnText[3], fg = "green").grid(row=0, column=3)
for ii in range(0,6):
    Label(top_frame, width=20, height=4, bg="green", text=labelText[ii]).grid(row=2, column=ii)
rowNum = rowNum + 1
get_rows()
tk.mainloop()