from tkinter import *
from .kalkulator import *

root = Tk()

"""
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Kalkulèr", fg="red")
button2 = Button(topFrame, text="Reset", fg="blue")
button3 = Button(topFrame, text="Kalkulèr", fg="green")
button4 = Button(botFrame, text="Kalkulèr", fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

# Widgets

one = Label(root, text="One", bg="white", fg="red")
one.pack()
two = Label(root, text="Two", bg="white", fg="red")
two.pack(fill=X)
three = Label(root, text="Three", bg="white", fg="red")
three.pack(side=LEFT, fill=Y)   

"""

kilometer = Label(root, text="Kilometer")
minutter = Label(root, text="Antall minutter")
entryKm = Entry(root)
entryMin = Entry(root)
calc = Button(root, text="Kalkulèr", fg="red")
calc.bind("<Button-1>", agderPris(entryKm, entryMin, 0, 0)


kilometer.grid(row=0, sticky=E)
minutter.grid(row=1, sticky=E)
entryKm.grid(row=0, column=1)
entryMin.grid(row=1, column=1)
calc.grid(columnspan=2, row=2)

root.mainloop()