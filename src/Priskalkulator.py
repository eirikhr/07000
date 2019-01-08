from tkinter import *
from functions import *

dateupdated = "08. Januar 2019 (Ordinære 2019 takster for AT og VT)"

calculator = Tk()
calculator.title("07000 Priskalkulator - Priser oppdatert: {}".format(dateupdated))
calculator.resizable(0, 0)


class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()


    def resetValues(self):
        self.createWidgets()


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

    def replaceVtNormS(self, text):
        self.resVtNormS.delete(0, END)
        self.resVtNormS.insert(0, text)

    def replaceVtNormM(self, text):
        self.resVtNormM.delete(0, END)
        self.resVtNormM.insert(0, text)

    def replaceVtNormL(self, text):
        self.resVtNormL.delete(0, END)
        self.resVtNormL.insert(0, text)

    def replaceVtKvelS(self, text):
        self.resVtKvelS.delete(0, END)
        self.resVtKvelS.insert(0, text)

    def replaceVtKvelM(self, text):
        self.resVtKvelM.delete(0, END)
        self.resVtKvelM.insert(0, text)

    def replaceVtKvelL(self, text):
        self.resVtKvelL.delete(0, END)
        self.resVtKvelL.insert(0, text)

    def replaceVtHelgS(self, text):
        self.resVtHelgS.delete(0, END)
        self.resVtHelgS.insert(0, text)

    def replaceVtHelgM(self, text):
        self.resVtHelgM.delete(0, END)
        self.resVtHelgM.insert(0, text)

    def replaceVtHelgL(self, text):
        self.resVtHelgL.delete(0, END)
        self.resVtHelgL.insert(0, text)

    def replaceVtHolyS(self, text):
        self.resVtHolyS.delete(0, END)
        self.resVtHolyS.insert(0, text)

    def replaceVtHolyM(self, text):
        self.resVtHolyM.delete(0, END)
        self.resVtHolyM.insert(0, text)

    def replaceVtHolyL(self, text):
        self.resVtHolyL.delete(0, END)
        self.resVtHolyL.insert(0, text)

    def replaceMtDagS(self, text):
        self.resMtDagS.delete(0, END)
        self.resMtDagS.insert(0, text)

    def replaceMtDagM(self, text):
        self.resMtDagM.delete(0, END)
        self.resMtDagM.insert(0, text)

    def replaceMtDagL(self, text):
        self.resMtDagL.delete(0, END)
        self.resMtDagL.insert(0, text)

    def replaceMtDagFremS(self, text):
        self.resMtDagFremS.delete(0, END)
        self.resMtDagFremS.insert(0, text)

    def replaceMtDagFremM(self, text):
        self.resMtDagFremM.delete(0, END)
        self.resMtDagFremM.insert(0, text)

    def replaceMtDagFremL(self, text):
        self.resMtDagFremL.delete(0, END)
        self.resMtDagFremL.insert(0, text)

    def replaceMtKvelS(self, text):
        self.resMtKvelS.delete(0, END)
        self.resMtKvelS.insert(0, text)

    def replaceMtKvelM(self, text):
        self.resMtKvelM.delete(0, END)
        self.resMtKvelM.insert(0, text)

    def replaceMtKvelL(self, text):
        self.resMtKvelL.delete(0, END)
        self.resMtKvelL.insert(0, text)

    def replaceMtLordS(self, text):
        self.resMtLordS.delete(0, END)
        self.resMtLordS.insert(0, text)

    def replaceMtLordM(self, text):
        self.resMtLordM.delete(0, END)
        self.resMtLordM.insert(0, text)

    def replaceMtLordL(self, text):
        self.resMtLordL.delete(0, END)
        self.resMtLordL.insert(0, text)

    def replaceMtHelgS(self, text):
        self.resMtHelgS.delete(0, END)
        self.resMtHelgS.insert(0, text)

    def replaceMtHelgM(self, text):
        self.resMtHelgM.delete(0, END)
        self.resMtHelgM.insert(0, text)

    def replaceMtHelgL(self, text):
        self.resMtHelgL.delete(0, END)
        self.resMtHelgL.insert(0, text)

    def replaceMtHolyS(self, text):
        self.resMtHolyS.delete(0, END)
        self.resMtHolyS.insert(0, text)

    def replaceMtHolyM(self, text):
        self.resMtHolyM.delete(0, END)
        self.resMtHolyM.insert(0, text)

    def replaceMtHolyL(self, text):
        self.resMtHolyL.delete(0, END)
        self.resMtHolyL.insert(0, text)

    def replaceMtKvelFremS(self, text):
        self.resMtKvelFremS.delete(0, END)
        self.resMtKvelFremS.insert(0, text)

    def replaceMtKvelFremM(self, text):
        self.resMtKvelFremM.delete(0, END)
        self.resMtKvelFremM.insert(0, text)

    def replaceMtKvelFremL(self, text):
        self.resMtKvelFremL.delete(0, END)
        self.resMtKvelFremL.insert(0, text)

    def replaceMtLordFremS(self, text):
        self.resMtLordFremS.delete(0, END)
        self.resMtLordFremS.insert(0, text)

    def replaceMtLordFremM(self, text):
        self.resMtLordFremM.delete(0, END)
        self.resMtLordFremM.insert(0, text)

    def replaceMtLordFremL(self, text):
        self.resMtLordFremL.delete(0, END)
        self.resMtLordFremL.insert(0, text)

    def replaceMtHelgFremS(self, text):
        self.resMtHelgFremS.delete(0, END)
        self.resMtHelgFremS.insert(0, text)

    def replaceMtHelgFremM(self, text):
        self.resMtHelgFremM.delete(0, END)
        self.resMtHelgFremM.insert(0, text)

    def replaceMtHelgFremL(self, text):
        self.resMtHelgFremL.delete(0, END)
        self.resMtHelgFremL.insert(0, text)

    def replaceMtHolyFremS(self, text):
        self.resMtHolyFremS.delete(0, END)
        self.resMtHolyFremS.insert(0, text)

    def replaceMtHolyFremM(self, text):
        self.resMtHolyFremM.delete(0, END)
        self.resMtHolyFremM.insert(0, text)

    def replaceMtHolyFremL(self, text):
        self.resMtHolyFremL.delete(0, END)
        self.resMtHolyFremL.insert(0, text)

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
            self.resultatVtNormS = int(vtNormS(self.inkm, self.inmin, self.intillegg))
            self.resultatVtNormM = int(vtNormM(self.inkm, self.inmin, self.intillegg))
            self.resultatVtNormL = int(vtNormL(self.inkm, self.inmin, self.intillegg))
            self.resultatVtKvelS = int(vtKvelS(self.inkm, self.inmin, self.intillegg))
            self.resultatVtKvelM = int(vtKvelM(self.inkm, self.inmin, self.intillegg))
            self.resultatVtKvelL = int(vtKvelL(self.inkm, self.inmin, self.intillegg))
            self.resultatVtHelgS = int(vtHelgS(self.inkm, self.inmin, self.intillegg))
            self.resultatVtHelgM = int(vtHelgM(self.inkm, self.inmin, self.intillegg))
            self.resultatVtHelgL = int(vtHelgL(self.inkm, self.inmin, self.intillegg))
            self.resultatVtHolyS = int(vtHolyS(self.inkm, self.inmin, self.intillegg))
            self.resultatVtHolyM = int(vtHolyM(self.inkm, self.inmin, self.intillegg))
            self.resultatVtHolyL = int(vtHolyL(self.inkm, self.inmin, self.intillegg))
            self.replaceVtNormS(self.resultatVtNormS)
            self.replaceVtNormM(self.resultatVtNormM)
            self.replaceVtNormL(self.resultatVtNormL)
            self.replaceVtKvelS(self.resultatVtKvelS)
            self.replaceVtKvelM(self.resultatVtKvelM)
            self.replaceVtKvelL(self.resultatVtKvelL)
            self.replaceVtHelgS(self.resultatVtHelgS)
            self.replaceVtHelgM(self.resultatVtHelgM)
            self.replaceVtHelgL(self.resultatVtHelgL)
            self.replaceVtHolyS(self.resultatVtHolyS)
            self.replaceVtHolyM(self.resultatVtHolyM)
            self.replaceVtHolyL(self.resultatVtHolyL)
            self.resultatMtDagS = int(mtDagS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtDagM = int(mtDagM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtDagL = int(mtDagL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtKvelS = int(mtKvelS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtKvelM = int(mtKvelM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtKvelL = int(mtKvelL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtLordS = int(mtLordS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtLordM = int(mtLordM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtLordL = int(mtLordL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHelgS = int(mtHelgS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHelgM = int(mtHelgM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHelgL = int(mtHelgL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHolyS = int(mtHolyS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHolyM = int(mtHolyM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHolyL = int(mtHolyL(self.inkm, self.inmin, self.infrem, self.intillegg))
            """
            self.resultatMtDagFremS = int(mtDagFremS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtDagFremM = int(mtDagFremM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtDagFremL = int(mtDagFremL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtKvelFremS = int(mtKvelFremS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtKvelFremM = int(mtKvelFremM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtKvelFremL = int(mtKvelFremL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtLordFremS = int(mtLordFremS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtLordFremM = int(mtLordFremM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtLordFremL = int(mtLordFremL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHelgFremS = int(mtHelgFremS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHelgFremM = int(mtHelgFremM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHelgFremL = int(mtHelgFremL(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHolyFremS = int(mtHolyFremS(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHolyFremM = int(mtHolyFremM(self.inkm, self.inmin, self.infrem, self.intillegg))
            self.resultatMtHolyFremL = int(mtHolyFremL(self.inkm, self.inmin, self.infrem, self.intillegg))
            """
            self.replaceMtDagS(self.resultatMtDagS)
            self.replaceMtDagM(self.resultatMtDagM)
            self.replaceMtDagL(self.resultatMtDagL)
            self.replaceMtKvelS(self.resultatMtKvelS)
            self.replaceMtKvelM(self.resultatMtKvelM)
            self.replaceMtKvelL(self.resultatMtKvelL)
            self.replaceMtLordS(self.resultatMtLordS)
            self.replaceMtLordM(self.resultatMtLordM)
            self.replaceMtLordL(self.resultatMtLordL)
            self.replaceMtHelgS(self.resultatMtHelgS)
            self.replaceMtHelgM(self.resultatMtHelgM)
            self.replaceMtHelgL(self.resultatMtHelgL)
            self.replaceMtHolyS(self.resultatMtHolyS)
            self.replaceMtHolyM(self.resultatMtHolyM)
            self.replaceMtHolyL(self.resultatMtHolyL)
            """
            self.replaceMtDagFremS(self.resultatMtDagFremS)
            self.replaceMtDagFremM(self.resultatMtDagFremM)
            self.replaceMtDagFremL(self.resultatMtDagFremL)
            self.replaceMtKvelFremS(self.resultatMtKvelFremS)
            self.replaceMtKvelFremM(self.resultatMtKvelFremM)
            self.replaceMtKvelFremL(self.resultatMtKvelFremL)
            self.replaceMtLordFremS(self.resultatMtLordFremS)
            self.replaceMtLordFremM(self.resultatMtLordFremM)
            self.replaceMtLordFremL(self.resultatMtLordFremL)
            self.replaceMtHelgFremS(self.resultatMtHelgFremS)
            self.replaceMtHelgFremM(self.resultatMtHelgFremM)
            self.replaceMtHelgFremL(self.resultatMtHelgFremL)
            self.replaceMtHolyFremS(self.resultatMtHolyFremS)
            self.replaceMtHolyFremM(self.resultatMtHolyFremM)
            self.replaceMtHolyFremL(self.resultatMtHolyFremL)
            """
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

        # Guide

        self.guideTextBox = LabelFrame(self, font=("Verdana", 10, "bold"), text="Bruksanvisning", relief=RIDGE)
        self.guideTextBox.grid(row=4, rowspan=11, column=2, columnspan=15)

        self.guideTidInfo = LabelFrame(self, font=("Verdana", 10, "bold"), text="Tidspunkt:", relief=RIDGE)
        self.guideTidInfo.grid(row=15, column=7)

        TidText = "AGDER TAXI:\n" \
                    "Hverdag: Man-Fre 06-20\n" \
                    "Kveld/Helg: Man-Tor 20-06\n" \
                    "Kveld/Helg: Fre f.o.m 20 til 06 Man\n" \
                    "Hellig: Påske- pinse-, jule- og nyttårsaften - høytid mellom 12-24.\n" \
                    "Andre høytids- og bevegelige helligdager - høytid hele døgnet.\n\n" \
                    \
                    "VENNESLA TAXI:\n" \
                    "Hverdag: Man-Fre 06-20\n" \
                    "Kveld: Man-Tor 06-20\n" \
                    "Kveld: Lør 06-18\n" \
                    "Kveld: Søn f.o.m 06 til 06 Man\n" \
                    "Helg: Fre-Lør 20-06\n" \
                    "Helg: Lør-Søn 18-06\n" \
                    "Hellig: Se Agder.\n\n" \
                    "" \
                    "MANDAL TAXI:\n" \
                    "Hverdag: Man-Fre 06-18\n" \
                    "Kveld: Man-Fre 18-24\n" \
                    "Lørdag: Lør 06-15\n" \
                    "Helg/Natt: Man-Fre 24-06\n" \
                    "Helg/Natt: Lør kl 15 til Man kl 06\n" \
                    "Hellig: Se Agder"


        self.guideTextAgder = Label(self.guideTidInfo, font=("Verdana", 8), text=TidText, justify=LEFT)
        self.guideTextAgder.grid(row=0, column=0)

        self.guideAnnetInfo = LabelFrame(self.guideTextBox, font=("Verdana", 10, "bold"), relief=RIDGE)
        self.guideAnnetInfo.grid(row=0, column=1)

        AnnetText = "FREMKJØRING:\n" \
                    "Gjelder kun Mandal. Ved tilkjøring ut over 10km fra nærmeste holdeplass\n" \
                    "kan bilene ta betalt tilkjøringstakst per kilometer.\n" \
                    "Eks: ved henting 13 kilometer fra nærmeste holdeplass\n" \
                    "legges tallet 3 inn i kalkulatoren til venstre.\n\n" \
                    "" \
                    "DIVERSE TILLEGG:\n" \
                    "Agder Taxi: Sykkeltillegg - 80,- kr.\n" \
                    "Agder Taxi: Rullestoltillegg - 131,- kr.\n"

        self.guideTextAnnet = Label(self.guideAnnetInfo, font=("Verdana", 8), text=AnnetText, justify=LEFT)
        self.guideTextAnnet.grid(row=0, column=0)



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

        self.seperator01 = Label(self.resultatAtTekst, text="-----------")
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

        self.seperator02 = Label(self.resultatAtTekst, text="-----------")
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

        self.seperator01 = Label(self.resultatVtTekst, text="-----------")
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

        self.seperator01 = Label(self.resultatVtTekst, text="-----------")
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

        # Mandal Taxi

        self.resultatMtTekst = LabelFrame(self, font=("Verdana", 10, "bold"), text="Mandal Taxi", relief=RIDGE)
        self.resultatMtTekst.grid(row=15, column=6, sticky="NWNESWSE")

        self.textMtDagS = Label(self.resultatMtTekst, font=("verdana", 8), text="1-4 PAX | Hverdag")
        self.textMtDagS.grid(row=1, column=2, sticky="W")
        self.resMtDagS = Entry(self.resultatMtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resMtDagS.insert(0, "0")
        self.resMtDagS.grid(row=1, column=3, sticky="NWNESWSE")

        self.textMtKvelS = Label(self.resultatMtTekst, font=("verdana", 8), fg="purple", text="1-4 PAX | Kveld")
        self.textMtKvelS.grid(row=2, column=2, sticky="W")
        self.resMtKvelS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
        self.resMtKvelS.insert(0, "0")
        self.resMtKvelS.grid(row=2, column=3, sticky="NWNESWSE")

        self.textMtLordS = Label(self.resultatMtTekst, font=("verdana", 8), fg="blue", text="1-4 PAX | Lørdag")
        self.textMtLordS.grid(row=3, column=2, sticky="W")
        self.resMtLordS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resMtLordS.insert(0, "0")
        self.resMtLordS.grid(row=3, column=3, sticky="NWNESWSE")

        self.textMtHelgS = Label(self.resultatMtTekst, font=("verdana", 8), fg="red", text="1-4 PAX | Helg/Natt")
        self.textMtHelgS.grid(row=4, column=2, sticky="W")
        self.resMtHelgS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resMtHelgS.insert(0, "0")
        self.resMtHelgS.grid(row=4, column=3, sticky="NWNESWSE")

        self.textMtHolyS = Label(self.resultatMtTekst, font=("verdana", 8), fg="gray", text="1-4 PAX | Hellig")
        self.textMtHolyS.grid(row=5, column=2, sticky="W")
        self.resMtHolyS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="gray", relief=RAISED, justify=RIGHT)
        self.resMtHolyS.insert(0, "0")
        self.resMtHolyS.grid(row=5, column=3, sticky="NWNESWSE")

        self.seperator96 = Label(self.resultatMtTekst, text="-----------")
        self.seperator96.grid(row=6, column=0, columnspan=4)

        self.textMtDagM = Label(self.resultatMtTekst, font=("verdana", 8), text="5-8 PAX | Hverdag")
        self.textMtDagM.grid(row=7, column=2, sticky="W")
        self.resMtDagM = Entry(self.resultatMtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resMtDagM.insert(0, "0")
        self.resMtDagM.grid(row=7, column=3, sticky="NWNESWSE")

        self.textMtKvelM = Label(self.resultatMtTekst, font=("verdana", 8), fg="purple", text="5-8 PAX | Kveld")
        self.textMtKvelM.grid(row=8, column=2, sticky="W")
        self.resMtKvelM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
        self.resMtKvelM.insert(0, "0")
        self.resMtKvelM.grid(row=8, column=3, sticky="NWNESWSE")

        self.textMtLordM = Label(self.resultatMtTekst, font=("verdana", 8), fg="blue", text="5-8 PAX | Lørdag")
        self.textMtLordM.grid(row=9, column=2, sticky="W")
        self.resMtLordM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resMtLordM.insert(0, "0")
        self.resMtLordM.grid(row=9, column=3, sticky="NWNESWSE")

        self.textMtHelgM = Label(self.resultatMtTekst, font=("verdana", 8), fg="red", text="5-8 PAX | Helg/Natt")
        self.textMtHelgM.grid(row=10, column=2, sticky="W")
        self.resMtHelgM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resMtHelgM.insert(0, "0")
        self.resMtHelgM.grid(row=10, column=3, sticky="NWNESWSE")

        self.textMtHolyM = Label(self.resultatMtTekst, font=("verdana", 8), fg="gray", text="5-8 PAX | Hellig")
        self.textMtHolyM.grid(row=11, column=2, sticky="W")
        self.resMtHolyM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="gray", relief=RAISED, justify=RIGHT)
        self.resMtHolyM.insert(0, "0")
        self.resMtHolyM.grid(row=11, column=3, sticky="NWNESWSE")

        self.seperator14 = Label(self.resultatMtTekst, text="-----------")
        self.seperator14.grid(row=12, column=0, columnspan=154)

        self.textMtDagL = Label(self.resultatMtTekst, font=("verdana", 8), text="9-16 PAX | Hverdag")
        self.textMtDagL.grid(row=13, column=2, sticky="W")
        self.resMtDagL = Entry(self.resultatMtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
        self.resMtDagL.insert(0, "0")
        self.resMtDagL.grid(row=13, column=3, sticky="NWNESWSE")

        self.textMtKvelL = Label(self.resultatMtTekst, font=("verdana", 8), fg="purple", text="9-16 PAX | Kveld")
        self.textMtKvelL.grid(row=14, column=2, sticky="W")
        self.resMtKvelL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
        self.resMtKvelL.insert(0, "0")
        self.resMtKvelL.grid(row=14, column=3, sticky="NWNESWSE")

        self.textMtLordL = Label(self.resultatMtTekst, font=("verdana", 8), fg="blue", text="9-16 PAX | Lørdag")
        self.textMtLordL.grid(row=15, column=2, sticky="W")
        self.resMtLordL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
        self.resMtLordL.insert(0, "0")
        self.resMtLordL.grid(row=15, column=3, sticky="NWNESWSE")

        self.textMtHelgL = Label(self.resultatMtTekst, font=("verdana", 8), fg="red", text="9-16 PAX | Helg/Natt")
        self.textMtHelgL.grid(row=16, column=2, sticky="W")
        self.resMtHelgL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
        self.resMtHelgL.insert(0, "0")
        self.resMtHelgL.grid(row=16, column=3, sticky="NWNESWSE")

        self.textMtHolyL = Label(self.resultatMtTekst, font=("verdana", 8), fg="gray", text="9-16 PAX | Hellig")
        self.textMtHolyL.grid(row=17, column=2, sticky="W")
        self.resMtHolyL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="gray", relief=RAISED, justify=RIGHT)
        self.resMtHolyL.insert(0, "0")
        self.resMtHolyL.grid(row=17, column=3, sticky="NWNESWSE")

        """

                self.resultatMtTekst = LabelFrame(self, font=("Verdana", 10, "bold"), text="Mandal Taxi med Fremmøte", relief=RIDGE)
                self.resultatMtTekst.grid(row=15, column=7, sticky="NWNESWSE")

                self.textMtDagFremS = Label(self.resultatMtTekst, font=("verdana", 8), text="1-4 PAX | Hverdag")
                self.textMtDagFremS.grid(row=1, column=2, sticky="W")
                self.resMtDagFremS = Entry(self.resultatMtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
                self.resMtDagFremS.insert(0, "0")
                self.resMtDagFremS.grid(row=1, column=3, sticky="NWNESWSE")

                self.textMtKvelFremS = Label(self.resultatMtTekst, font=("verdana", 8), fg="purple", text="1-4 PAX | Kveld")
                self.textMtKvelFremS.grid(row=2, column=2, sticky="W")
                self.resMtKvelFremS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
                self.resMtKvelFremS.insert(0, "0")
                self.resMtKvelFremS.grid(row=2, column=3, sticky="NWNESWSE")

                self.textMtLordFremS = Label(self.resultatMtTekst, font=("verdana", 8), fg="blue", text="1-4 PAX | Lørdag")
                self.textMtLordFremS.grid(row=3, column=2, sticky="W")
                self.resMtLordFremS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
                self.resMtLordFremS.insert(0, "0")
                self.resMtLordFremS.grid(row=3, column=3, sticky="NWNESWSE")

                self.textMtHelgFremS = Label(self.resultatMtTekst, font=("verdana", 8), fg="red", text="1-4 PAX | Helg/Natt")
                self.textMtHelgFremS.grid(row=4, column=2, sticky="W")
                self.resMtHelgFremS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
                self.resMtHelgFremS.insert(0, "0")
                self.resMtHelgFremS.grid(row=4, column=3, sticky="NWNESWSE")

                self.textMtHolyFremS = Label(self.resultatMtTekst, font=("verdana", 8), fg="gray", text="1-4 PAX | Hellig")
                self.textMtHolyFremS.grid(row=5, column=2, sticky="W")
                self.resMtHolyFremS = Entry(self.resultatMtTekst, font=("Arial", 8), fg="gray", relief=RAISED, justify=RIGHT)
                self.resMtHolyFremS.insert(0, "0")
                self.resMtHolyFremS.grid(row=5, column=3, sticky="NWNESWSE")

                self.seperator96 = Label(self.resultatMtTekst, text="-----------")
                self.seperator96.grid(row=6, column=0, columnspan=4)

                self.textMtDagFremM = Label(self.resultatMtTekst, font=("verdana", 8), text="5-8 PAX | Hverdag")
                self.textMtDagFremM.grid(row=7, column=2, sticky="W")
                self.resMtDagFremM = Entry(self.resultatMtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
                self.resMtDagFremM.insert(0, "0")
                self.resMtDagFremM.grid(row=7, column=3, sticky="NWNESWSE")

                self.textMtKvelFremM = Label(self.resultatMtTekst, font=("verdana", 8), fg="purple", text="5-8 PAX | Kveld")
                self.textMtKvelFremM.grid(row=8, column=2, sticky="W")
                self.resMtKvelFremM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
                self.resMtKvelFremM.insert(0, "0")
                self.resMtKvelFremM.grid(row=8, column=3, sticky="NWNESWSE")

                self.textMtLordFremM = Label(self.resultatMtTekst, font=("verdana", 8), fg="blue", text="5-8 PAX | Lørdag")
                self.textMtLordFremM.grid(row=9, column=2, sticky="W")
                self.resMtLordFremM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
                self.resMtLordFremM.insert(0, "0")
                self.resMtLordFremM.grid(row=9, column=3, sticky="NWNESWSE")

                self.textMtHelgFremM = Label(self.resultatMtTekst, font=("verdana", 8), fg="red", text="5-8 PAX | Helg/Natt")
                self.textMtHelgFremM.grid(row=10, column=2, sticky="W")
                self.resMtHelgFremM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
                self.resMtHelgFremM.insert(0, "0")
                self.resMtHelgFremM.grid(row=10, column=3, sticky="NWNESWSE")

                self.textMtHolyFremM = Label(self.resultatMtTekst, font=("verdana", 8), fg="gray", text="5-8 PAX | Hellig")
                self.textMtHolyFremM.grid(row=11, column=2, sticky="W")
                self.resMtHolyFremM = Entry(self.resultatMtTekst, font=("Arial", 8), fg="gray", relief=RAISED, justify=RIGHT)
                self.resMtHolyFremM.insert(0, "0")
                self.resMtHolyFremM.grid(row=11, column=3, sticky="NWNESWSE")

                self.seperator14 = Label(self.resultatMtTekst, text="-----------")
                self.seperator14.grid(row=12, column=0, columnspan=154)

                self.textMtDagFremL = Label(self.resultatMtTekst, font=("verdana", 8), text="9-16 PAX | Hverdag")
                self.textMtDagFremL.grid(row=13, column=2, sticky="W")
                self.resMtDagFremL = Entry(self.resultatMtTekst, font=("Arial", 8), relief=RAISED, justify=RIGHT)
                self.resMtDagFremL.insert(0, "0")
                self.resMtDagFremL.grid(row=13, column=3, sticky="NWNESWSE")

                self.textMtKvelFremL = Label(self.resultatMtTekst, font=("verdana", 8), fg="purple", text="9-16 PAX | Kveld")
                self.textMtKvelFremL.grid(row=14, column=2, sticky="W")
                self.resMtKvelFremL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="purple", relief=RAISED, justify=RIGHT)
                self.resMtKvelFremL.insert(0, "0")
                self.resMtKvelFremL.grid(row=14, column=3, sticky="NWNESWSE")

                self.textMtLordFremL = Label(self.resultatMtTekst, font=("verdana", 8), fg="blue", text="9-16 PAX | Lørdag")
                self.textMtLordFremL.grid(row=15, column=2, sticky="W")
                self.resMtLordFremL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="blue", relief=RAISED, justify=RIGHT)
                self.resMtLordFremL.insert(0, "0")
                self.resMtLordFremL.grid(row=15, column=3, sticky="NWNESWSE")

                self.textMtHelgFremL = Label(self.resultatMtTekst, font=("verdana", 8), fg="red", text="9-16 PAX | Helg/Natt")
                self.textMtHelgFremL.grid(row=16, column=2, sticky="W")
                self.resMtHelgFremL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="red", relief=RAISED, justify=RIGHT)
                self.resMtHelgFremL.insert(0, "0")
                self.resMtHelgFremL.grid(row=16, column=3, sticky="NWNESWSE")

                self.textMtHolyFremL = Label(self.resultatMtTekst, font=("verdana", 8), fg="gray", text="9-16 PAX | Hellig")
                self.textMtHolyFremL.grid(row=17, column=2, sticky="W")
                self.resMtHolyFremL = Entry(self.resultatMtTekst, font=("Arial", 8), fg="gray", relief=RAISED, justify=RIGHT)
                self.resMtHolyFremL.insert(0, "0")
                self.resMtHolyFremL.grid(row=17, column=3, sticky="NWNESWSE")

                """


app = Application(calculator).grid()
calculator.mainloop()