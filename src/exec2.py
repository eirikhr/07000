from tkinter import *
from functions import *

dateupdated = "23. November 2018"

calculator = Tk()
calculator.title("07000 Priskalkulator - Priser oppdatert: {}".format(dateupdated))
calculator.resizable(0, 0)


class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    def resetValues(self):
        self.kmEntry.delete(0, END)
        self.kmEntry.insert(0, "0")
        self.minEntry.delete(0, END)
        self.minEntry.insert(0, "0")
        self.fremEntry.delete(0, END)
        self.fremEntry.insert(0, "0")
        self.tilleggEntry.delete(0, END)
        self.tilleggEntry.insert(0, "0")
        self.resAtNormS.delete(0, END)
        self.resAtNormS.insert(0, "0")
        self.resAtNormM.delete(0, END)
        self.resAtNormM.insert(0, "0")
        self.resAtNormL.delete(0, END)
        self.resAtNormL.insert(0, "0")
        self.resAtHelgS.delete(0, END)
        self.resAtHelgS.insert(0, "0")
        self.resAtHelgM.delete(0, END)
        self.resAtHelgM.insert(0, "0")
        self.resAtHelgL.delete(0, END)
        self.resAtHelgL.insert(0, "0")
        self.resAtHolyS.delete(0, END)
        self.resAtHolyS.insert(0, "0")
        self.resAtHolyM.delete(0, END)
        self.resAtHolyM.insert(0, "0")
        self.resAtHolyL.delete(0, END)
        self.resAtHolyL.insert(0, "0")


    def replaceAtNormS(self, text):
        self.resAtNormS.delete(0, END)
        self.resAtNormS.insert(0, text)

    def replaceAtNormM(self, text):
        self.resAtNormM.delete(0, END)
        self.resAtNormM.insert(0, text)

    def replaceAtNormL(self, text):
        self.resAtNormL.delete(0, END)
        self.resAtNormL.insert(0, text)

    def replaceAtHelgS(self, text):
        self.resAtHelgS.delete(0, END)
        self.resAtHelgS.insert(0, text)

    def replaceAtHelgM(self, text):
        self.resAtHelgM.delete(0, END)
        self.resAtHelgM.insert(0, text)

    def replaceAtHelgL(self, text):
        self.resAtHelgL.delete(0, END)
        self.resAtHelgL.insert(0, text)

    def replaceAtHolyS(self, text):
        self.resAtHolyS.delete(0, END)
        self.resAtHolyS.insert(0, text)

    def replaceAtHolyM(self, text):
        self.resAtHolyM.delete(0, END)
        self.resAtHolyM.insert(0, text)

    def replaceAtHolyL(self, text):
        self.resAtHolyL.delete(0, END)
        self.resAtHolyL.insert(0, text)

    def calculateAll(self):
        self.inkm = float(self.kmEntry.get())
        self.inmin = float(self.minEntry.get())
        self.infrem = float(self.fremEntry.get())
        self.intillegg = float(self.tilleggEntry.get())

        try:
            self.resultatAtNormS = int(atNormS(self.inkm, self.inmin, self.intillegg))
            self.resultatAtNormM = int(atNormM(self.inkm, self.inmin, self.intillegg))
            self.resultatAtNormL = int(atNormL(self.inkm, self.inmin, self.intillegg))
            self.resultatAtHelgS = int(atHelgS(self.inkm, self.inmin, self.intillegg))
            self.resultatAtHelgM = int(atHelgM(self.inkm, self.inmin, self.intillegg))
            self.resultatAtHelgL = int(atHelgL(self.inkm, self.inmin, self.intillegg))
            self.resultatAtHolyS = int(atHolyS(self.inkm, self.inmin, self.intillegg))
            self.resultatAtHolyM = int(atHolyM(self.inkm, self.inmin, self.intillegg))
            self.resultatAtHolyL = int(atHolyL(self.inkm, self.inmin, self.intillegg))

            self.replaceAtNormS(self.resultatAtNormS)
            self.replaceAtNormM(self.resultatAtNormM)
            self.replaceAtNormL(self.resultatAtNormL)
            self.replaceAtHelgS(self.resultatAtHelgS)
            self.replaceAtHelgM(self.resultatAtHelgM)
            self.replaceAtHelgL(self.resultatAtHelgL)
            self.replaceAtHolyS(self.resultatAtHolyS)
            self.replaceAtHolyM(self.resultatAtHolyM)
            self.replaceAtHolyL(self.resultatAtHolyL)


        except:
            messagebox.showinfo("Error", "Invalid input")



    def createWidgets(self):

        # Entries

        self.kmLabel = Label(self, font=("verdana", 10), text="Kilometer:")
        self.kmLabel.grid(row=4, column=0)

        self.kmEntry = Entry(self, font=("verdana", 10), relief=RAISED, justify=RIGHT)
        self.kmEntry.insert(0, "0")
        self.kmEntry.grid(row=4, column=1)

        self.minLabel = Label(self, font=("verdana", 10), text="Minutter:")
        self.minLabel.grid(row=5, column=0)

        self.minEntry = Entry(self, font=("verdana", 10), relief=RAISED, justify=RIGHT)
        self.minEntry.insert(0, "0")
        self.minEntry.grid(row=5, column=1)

        self.fremLabel = Label(self, font=("verdana", 10), text="Fremkjøring km:")
        self.fremLabel.grid(row=6, column=0)

        self.fremEntry = Entry(self, font=("verdana", 10), relief=RAISED, justify=RIGHT)
        self.fremEntry.insert(0, "0")
        self.fremEntry.grid(row=6, column=1)

        self.tilleggLabel = Label(self, font=("verdana", 10), text="Tillegg kr:")
        self.tilleggLabel.grid(row=7, column=0)

        self.tilleggEntry = Entry(self, font=("verdana", 10), relief=RAISED, justify=RIGHT)
        self.tilleggEntry.insert(0, "0")
        self.tilleggEntry.grid(row=7, column=1)

        # Buttons

        self.calculateButton = Button(self, font=("verdana", 10), text="Kalkulèr", command=lambda: self.calculateAll())
        self.calculateButton.grid(row=10, column=0, columnspan=1, sticky="NWNESWSE")
        self.resetButton = Button(self, font=("verdana", 10), text="Nullstill", command=lambda: self.resetValues())
        self.resetButton.grid(row=10, column=1, columnspan=1, sticky="NWNESWSE")

        # Results

        # AGDER TAXI

        self.resultatAtTekst = LabelFrame(self, font=("Verdana", 10, "bold"), text="Agder Taxi", relief=RIDGE)
        self.resultatAtTekst.grid(row=15, column=0, sticky="NWNESWSE")

        self.textAtNormS = Label(self.resultatAtTekst, font=("verdana", 8), text="1-4 PAX | Hverdag")
        self.textAtNormS.grid(row=20, column=2, sticky="W")
        self.resAtNormS = Entry(self.resultatAtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resAtNormS.insert(0, "0")
        self.resAtNormS.grid(row=20, column=3, sticky="NWNESWSE")

        self.textAtHelgS = Label(self.resultatAtTekst, font=("verdana", 8), fg="blue", text="1-4 PAX | Kveld/Helg")
        self.textAtHelgS.grid(row=21, column=2, sticky="W")
        self.resAtHelgS = Entry(self.resultatAtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resAtHelgS.insert(0, "0")
        self.resAtHelgS.grid(row=21, column=3, sticky="NWNESWSE")

        self.textAtHolyS = Label(self.resultatAtTekst, font=("verdana", 8), fg="red", text="1-4 PAX | Helligdag")
        self.textAtHolyS.grid(row=22, column=2, sticky="W")
        self.resAtHolyS = Entry(self.resultatAtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resAtHolyS.insert(0, "0")
        self.resAtHolyS.grid(row=22, column=3, sticky="NWNESWSE")

        self.seperator01 = Label(self.resultatAtTekst, text="")
        self.seperator01.grid(row=23, column=0, columnspan=4)

        self.textAtNormM = Label(self.resultatAtTekst, font=("verdana", 8), text="5-8 PAX | Hverdag")
        self.textAtNormM.grid(row=24, column=2, sticky="W")
        self.resAtNormM = Entry(self.resultatAtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resAtNormM.insert(0, "0")
        self.resAtNormM.grid(row=24, column=3, sticky="NWNESWSE")

        self.textAtHelgM = Label(self.resultatAtTekst, font=("verdana", 8), fg="blue", text="5-8 PAX | Kveld/Helg")
        self.textAtHelgM.grid(row=25, column=2, sticky="W")
        self.resAtHelgM = Entry(self.resultatAtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resAtHelgM.insert(0, "0")
        self.resAtHelgM.grid(row=25, column=3, sticky="NWNESWSE")

        self.textAtHolyM = Label(self.resultatAtTekst, font=("verdana", 8), fg="red", text="5-8 PAX | Helligdag")
        self.textAtHolyM.grid(row=26, column=2, sticky="W")
        self.resAtHolyM = Entry(self.resultatAtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resAtHolyM.insert(0, "0")
        self.resAtHolyM.grid(row=26, column=3, sticky="NWNESWSE")

        self.seperator02 = Label(self.resultatAtTekst, text="")
        self.seperator02.grid(row=27, column=0, columnspan=4)

        self.textAtNormL = Label(self.resultatAtTekst, font=("verdana", 8), text="9-16 PAX | Hverdag")
        self.textAtNormL.grid(row=28, column=2, sticky="W")
        self.resAtNormL = Entry(self.resultatAtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resAtNormL.insert(0, "0")
        self.resAtNormL.grid(row=28, column=3, sticky="NWNESWSE")

        self.textAtHelgL = Label(self.resultatAtTekst, font=("verdana", 8), fg="blue", text="9-16 PAX | Kveld/Helg")
        self.textAtHelgL.grid(row=29, column=2, sticky="W")
        self.resAtHelgL = Entry(self.resultatAtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resAtHelgL.insert(0, "0")
        self.resAtHelgL.grid(row=29, column=3, sticky="NWNESWSE")

        self.textAtHolyL = Label(self.resultatAtTekst, font=("verdana", 8), fg="red", text="9-16 PAX | Helligdag")
        self.textAtHolyL.grid(row=30, column=2, sticky="W")
        self.resAtHolyL = Entry(self.resultatAtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resAtHolyL.insert(0, "0")
        self.resAtHolyL.grid(row=30, column=3, sticky="NWNESWSE")




        # VENNESLA TAXI



        self.resultatVtTekst = LabelFrame(self, font=("Verdana", 10, "bold"), text="Vennesla Taxi", relief=RIDGE)
        self.resultatVtTekst.grid(row=15, column=1, sticky="NWNESWSE")



        self.textVtNormS = Label(self.resultatVtTekst, font=("verdana", 8), text="1-4 PAX | Hverdag")
        self.textVtNormS.grid(row=1, column=2, sticky="W")
        self.resVtNormS = Entry(self.resultatVtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resVtNormS.insert(0, "0")
        self.resVtNormS.grid(row=1, column=3, sticky="NWNESWSE")

        self.textVtKvelS = Label(self.resultatVtTekst, font=("verdana", 8), fg="purple", text="1-4 PAX | Kveld")
        self.textVtKvelS.grid(row=2, column=2, sticky="W")
        self.resVtKvelS = Entry(self.resultatVtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
        self.resVtKvelS.insert(0, "0")
        self.resVtKvelS.grid(row=2, column=3, sticky="NWNESWSE")

        self.textVtHelgS = Label(self.resultatVtTekst, font=("verdana", 8), fg="blue", text="1-4 PAX | Helg")
        self.textVtHelgS.grid(row=3, column=2, sticky="W")
        self.resVtHelgS = Entry(self.resultatVtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resVtHelgS.insert(0, "0")
        self.resVtHelgS.grid(row=3, column=3, sticky="NWNESWSE")

        self.textVtHolyS = Label(self.resultatVtTekst, font=("verdana", 8), fg="red", text="1-4 PAX | Helligdag")
        self.textVtHolyS.grid(row=4, column=2, sticky="W")
        self.resVtHolyS = Entry(self.resultatVtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resVtHolyS.insert(0, "0")
        self.resVtHolyS.grid(row=4, column=3, sticky="NWNESWSE")

        self.seperator01 = Label(self.resultatVtTekst, text="")
        self.seperator01.grid(row=5, column=0, columnspan=4)

        self.textVtNormM = Label(self.resultatVtTekst, font=("verdana", 8), text="5-8 PAX | Hverdag")
        self.textVtNormM.grid(row=6, column=2, sticky="W")
        self.resVtNormM = Entry(self.resultatVtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resVtNormM.insert(0, "0")
        self.resVtNormM.grid(row=6, column=3, sticky="NWNESWSE")

        self.textVtKvelM = Label(self.resultatVtTekst, font=("verdana", 8), fg="purple", text="5-8 PAX | Kveld")
        self.textVtKvelM.grid(row=7, column=2, sticky="W")
        self.resVtKvelM = Entry(self.resultatVtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
        self.resVtKvelM.insert(0, "0")
        self.resVtKvelM.grid(row=7, column=3, sticky="NWNESWSE")

        self.textVtHelgM = Label(self.resultatVtTekst, font=("verdana", 8), fg="blue", text="5-8 PAX | Helg")
        self.textVtHelgM.grid(row=8, column=2, sticky="W")
        self.resVtHelgM = Entry(self.resultatVtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resVtHelgM.insert(0, "0")
        self.resVtHelgM.grid(row=8, column=3, sticky="NWNESWSE")

        self.textVtHolyM = Label(self.resultatVtTekst, font=("verdana", 8), fg="red", text="5-8 PAX | Helligdag")
        self.textVtHolyM.grid(row=9, column=2, sticky="W")
        self.resVtHolyM = Entry(self.resultatVtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resVtHolyM.insert(0, "0")
        self.resVtHolyM.grid(row=9, column=3, sticky="NWNESWSE")

        self.seperator01 = Label(self.resultatVtTekst, text="")
        self.seperator01.grid(row=10, column=0, columnspan=4)

        self.textVtNormL = Label(self.resultatVtTekst, font=("verdana", 8), text="9-16 PAX | Hverdag")
        self.textVtNormL.grid(row=11, column=2, sticky="W")
        self.resVtNormL = Entry(self.resultatVtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resVtNormL.insert(0, "0")
        self.resVtNormL.grid(row=11, column=3, sticky="NWNESWSE")

        self.textVtKvelL = Label(self.resultatVtTekst, font=("verdana", 8), fg="purple", text="9-16 PAX | Kveld")
        self.textVtKvelL.grid(row=12, column=2, sticky="W")
        self.resVtKvelL = Entry(self.resultatVtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
        self.resVtKvelL.insert(0, "0")
        self.resVtKvelL.grid(row=12, column=3, sticky="NWNESWSE")

        self.textVtHelgL = Label(self.resultatVtTekst, font=("verdana", 8), fg="blue", text="9-16 PAX | Helg")
        self.textVtHelgL.grid(row=13, column=2, sticky="W")
        self.resVtHelgL = Entry(self.resultatVtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resVtHelgL.insert(0, "0")
        self.resVtHelgL.grid(row=13, column=3, sticky="NWNESWSE")

        self.textVtHolyL = Label(self.resultatVtTekst, font=("verdana", 8), fg="red", text="9-16 PAX | Helligdag")
        self.textVtHolyL.grid(row=14, column=2, sticky="W")
        self.resVtHolyL = Entry(self.resultatVtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resVtHolyL.insert(0, "0")
        self.resVtHolyL.grid(row=14, column=3, sticky="NWNESWSE")




app = Application(calculator).grid()
calculator.mainloop()