from tkinter import *
import tkinter
print ("e")
tk = Tk()
namR = []
data = []
rowNum = 1
columnNum=0
i = 0
def create_row():
    global rowNum
    global columnNum
    global namR
    global data
    columnNum=0 # we set columnnum to 0 to start creating rows from the left
    print([e.get() for e in namR]) #debug purposes
    for ii in range(0,4):
        namR.append(Entry(tk))
        namR[ii].grid(row=rowNum, column=columnNum)
        columnNum = columnNum + 1
    rowNum = rowNum + 1
    for e in namR:
        data.append(e)
        print([e.get() for e in data])
    namR = [] 
    print([e.get() for e in data])

def delete_row():
    print(reversed(list(enumerate(rows))))
btnText = ["Afegir medicament","Treure medicament","Extra"]
labelText = ["Nom medicament","Data medicament","Cuantitat","Hores"]
bottom_frame = tkinter.Frame(tk).grid(row=0, column=0)
for ii in range(0,3):
    tkinter.Button(bottom_frame, text = btnText[ii], fg = "green", command = create_row).grid(row=0, column=ii)
for ii in range(0,4):
    Label(tk, width=20, height=4, bg="green", text=labelText[ii]).grid(row=1, column=ii)
rowNum = rowNum + 1
create_row()
tk.mainloop()
