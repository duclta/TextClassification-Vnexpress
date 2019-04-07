from tkinter import *
import os
import subprocess
import fastText

frmMain = Tk()
frmMain.title("Text Classification")

customFont = ('', 20, 'bold')
customFont1 = ('', 15)

lb1 = Label(frmMain, text = "Input", font = customFont)
lb1.pack()

tbInput = Text(frmMain, height = 30, font = customFont1)
tbInput.pack()

lb2 = Label(frmMain, text = "Category", font = customFont)
lb2.pack()

tbOutput1 = Entry(frmMain, width = 30, font = customFont1)
tbOutput1.pack()

lb3 = Label(frmMain, text = "Precision", font = customFont)
lb3.pack()

tbOutput2 = Entry(frmMain, width = 30, font = customFont1)
tbOutput2.pack()

def btnSubmit_Click():
    model = fastText.load_model("model_vnexpress.bin")
    strInput = tbInput.get(1.0, END).strip().replace('\n'," ").lower()
    strOutput1 = ''.join(model.predict(strInput)[0]).replace("__label__", "").replace("-"," ")
    strOutput2 = model.predict(strInput)[1][0]
    tbOutput1.delete(0, END)
    tbOutput1.insert(0, strOutput1)
    tbOutput2.delete(0, END)
    tbOutput2.insert(0, strOutput2)


btnSubmit = Button(frmMain, text = "Submit", font = customFont1, command = btnSubmit_Click)
btnSubmit.pack()

frmMain.mainloop()