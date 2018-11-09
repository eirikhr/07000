import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(n1)+int(n2)
    label_result.config(text="Result is %d" % result)
    return

root = tk.Tk()
root.geometry('400x200+100+200')
root.title('07000 Taxikalkulator')

idKm = tk.StringVar()
idMin = tk.StringVar()

labelTitle = tk.Label(root, text="07000 Kalkulator")
labelTitle.grid(row=0)

labelKilometer = tk.Label(root, text="Antall kilometer")
labelKilometer.grid(row=1, column=0)
entryKilometer = tk.Entry(root, textvariable=idKm)
entryKilometer.grid(row=1, column=1)

labelMinutt = tk.Label(root, text="Antall minutter")
labelMinutt.grid(row=2, column=0)
entryMinutt = tk.Entry(root, textvariable=idMin)
entryMinutt.grid(row=2, column=1)

labelResult = tk.Label(root)
labelResult.grid(row=5, column=2)

call_result = partial(call_result, labelResult, idKm, idMin)
buttonCal = tk.Button(root, text="Kalkulèr", command=call_result)
buttonCal.grid(row=3, column=0)

root.mainloop()