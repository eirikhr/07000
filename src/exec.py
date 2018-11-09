import tkinter as tk
from functions import *


root = tk.Tk()
root.geometry('400x200+100+200')
root.title('07000 Priskalkulator')

idKm = tk.IntVar()
idMin = tk.IntVar()
idOver = tk.IntVar()
idFrem = tk.IntVar()
idTillegg = tk.IntVar()

labelTitle = tk.Label(root, text="07000 Kalkulator")
labelTitle.grid(row=0)
labelIntro = tk.Label(root, text="Lang tekst som forklarer bla bla blasdjhashbdasd \nasjhd asbdha shasd asdh ashdsah ads"
                                 "dhsahdsah dsah dashd ashd a\nshdas hdsahd ash sahd asdas asd as"
                                 "s dahdsahda shadh asdhsa")
labelIntro.grid(row=0, columnspan=6)

labelKilometer = tk.Label(root, text="Antall kilometer")
labelKilometer.grid(row=1, column=0)
entryKilometer = tk.Entry(root, textvariable=idKm)
entryKilometer.grid(row=1, column=1)

labelMinutt = tk.Label(root, text="Antall minutter")
labelMinutt.grid(row=2, column=0)
entryMinutt = tk.Entry(root, textvariable=idMin)
entryMinutt.grid(row=2, column=1)

labelOver = tk.Label(root, text="Antall km over")
labelOver.grid(row=3, column=0)
entryOver = tk.Entry(root, textvariable=idOver)
entryOver.grid(row=3, column=1)

buttonCal = tk.Button(root, text="Kalkulèr")
buttonCal.grid(row=10, column=0)

# Denne funker ikke enda!!!
# labelResult1 = tk.Label(root, command=atNormS(int(idKm), int(idMin), int(idTillegg)))

root.mainloop()
