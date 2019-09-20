from tkinter import *
import sqlite3
import datetime
from tkinter import messagebox
import tkinter
tk = Tk()
namR = []
data = []
rowNum = 2 #we define the row to start creating the grids
db_data = []
select_data = []
m_id = []
checkbox = []
temp_data = []
temp_patients = []
original_data = []
new_data = []
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

def push_changes():
    new_data = []
    i = 0
    dbRowNum = 0
    for ii in data:
        new_data.append(ii.get())
    print(new_data[1])
    print(original_data[1])
    for ii in original_data:
        if ii != new_data[i]:
            change = 1
        i = i + 1
        if i == 6:
            if change == 1:
                conn = sqlite3.connect('db.db')
                print(m_id)
                params = (new_data[0],new_data[1],new_data[2],new_data[3],new_data[4],new_data[5],str(m_id[dbRowNum]))
                conn.execute('UPDATE medicaments SET mName = ?, mDosi = ?, mPauta = ?, mDataInici = ?, mDataFinal = ?, mObservacions = ? WHERE mId = ? ',params)
                conn.commit()
                for ii in range(0,6):
                    new_data.pop()
                    original_data.pop()
                    change = 0
            dbRowNum = dbRowNum + 1
            i = 0


def get_rows(patient):
    global namR
    global rowNum
    global i 
    i = 0
    conn = sqlite3.connect('db.db')
    params = (patient,)
    cursor = conn.execute("SELECT * FROM medicaments where mPatientName = ? ",params)
    for row in cursor:
        m_id.append(str(row[0]))
        dataRow = [row[9],row[8],row[7],row[6],row[5],row[4]]
        original_data.extend((row[4],row[5],row[6],row[7],row[8],row[9]))
        select_data.append(dataRow)
        create_row()
        for ii in dataRow:
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
def load_client(patient):
    global popup
    popup.destroy()
    global rowNum
    global tkinter
    top_frame = tkinter.Frame(tk).grid(row=0, column=0)
    btnText = ["Afegir medicament","Treure medicament","Extra","TEST"]
    labelText = ["Nom medicament","Dosi","Pauta","Data inici","Data final","Observacions"]
    tkinter.Button(top_frame, text = btnText[0], fg = "green", command = create_row).grid(row=0, column=0)
    tkinter.Button(top_frame, text = btnText[1], fg = "green", command = destroy_row).grid(row=0, column=1)
    tkinter.Button(top_frame, text = btnText[2], fg = "green", command = push_changes).grid(row=0, column=2)
    tkinter.Button(top_frame, text = btnText[3], fg = "green").grid(row=0, column=3)
    for ii in range(0,6):
        Label(top_frame, width=20, height=4, bg="green", text=labelText[ii]).grid(row=2, column=ii)
    rowNum = rowNum + 1
    get_rows(patient)
def popup():
    global popup
    def popupsearch():
        for item in temp_patients:
            item.destroy()
        conn = sqlite3.connect('db.db')
        params = (SearchName.get(),)
        cursor = conn.execute("SELECT * FROM patient where pName = ? ",params)
        for row in cursor:
            temp_patients.append(Button(popup, width=30, height=2, bg="yellow",text=row[2]+","+row[3]+","+row[4]+","+row[5],command= lambda: load_client(row[2])))
            temp_patients[-1].pack()
    popup = Toplevel()
    Label(popup, width=20, height=4, bg="green", text="Nom client").pack(side="top")
    SearchName =  Entry(popup, width=20)
    SearchName.pack(side="top")
    tkinter.Button(popup,text = "Buscar clients",command = popupsearch).pack()
popup()
tk.mainloop()