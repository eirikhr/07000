# AGDER TAXI
# HVERDAGSTAKSTER

atNormStartS = 69                # 1-4  Startpris
atNormStartM = 104               # 5-8  Startpris 5-8
atNormStartL = 137               # 9-16 Startpris
atNormKmS = 13.65                # 1-4  Kroner per kilometer
atNormKmM = 24.1                 # 5-8  Kroner per kilometer
atNormKmL = 34.6                 # 9-16 Kroner per kilometer
atNormKmOverM = 19.5             # 5-8  Kroner per kilometer over 30km
atNormKmOverL = 27.7             # 9-16 Kroner per kilometer over 30km
atNormTid = 7.85                 # Minuttpris
atNormMinstS = 114               # 1-4  Minstepris
atNormMinstM = 170               # 5-8  Minstepris
atNormMinstL = 226               # 9-16 Minstepris

# KVELD OG HELGETAKSTER

atHelgStartS = 90                # 1-4  Startpris
atHelgStartM = 135               # 5-8  Startpris 5-8
atHelgStartL = 178               # 9-16 Startpris
atHelgKmS = 17.75                # 1-4  Kroner per kilometer
atHelgKmM = 31.35                # 5-8  Kroner per kilometer
atHelgKmL = 44.95                # 9-16 Kroner per kilometer
atHelgKmOverM = 25.35            # 5-8  Kroner per kilometer over 30km
atHelgKmOverL = 36               # 9-16 Kroner per kilometer over 30km
atHelgTid = 10.2                 # Minuttpris
atHelgMinstS = 148               # 1-4  Minstepris
atHelgMinstM = 221               # 5-8  Minstepris
atHelgMinstL = 294               # 9-16 Minstepris

# HELLIGTAKSTER

atHolyStartS = 104               # 1-4  Startpris
atHolyStartM = 156               # 5-8  Startpris 5-8
atHolyStartL = 206               # 9-16 Startpris
atHolyKmS = 20.45                # 1-4  Kroner per kilometer
atHolyKmM = 36.15                # 5-8  Kroner per kilometer
atHolyKmL = 51.9                 # 9-16 Kroner per kilometer
atHolyKmOverM = 29.25            # 5-8  Kroner per kilometer over 30km
atHolyKmOverL = 41.55            # 9-16 Kroner per kilometer over 30km
atHolyTid = 11.75                # Minuttpris
atHolyMinstS = 114               # 1-4  Minstepris
atHolyMinstM = 255               # 5-8  Minstepris
atHolyMinstL = 339               # 9-16 Minstepris


def agderPris(inputkm, inputtid, inputkmover, inputtillegg):
    print()
    print("Prisberegning for en tur på \n{} kilometer (+ {} km over 3 mil ved buss)\n{} minutter \n{},- kroner i tilegg."
          .format(inputkm, inputkmover, inputtid, inputtillegg))
    print()
    print("HVERDAGER 06:00 - 20:00")
    print("1-4 Passasjerer")
    resultat = (inputkm * atNormKmS) + (inputtid * atNormTid) + atNormStartS + inputtillegg
    if resultat < atNormMinstS:
        resultat = atNormMinstS
    print("{},- kroner\n".format(int(resultat)))

    print("5-8 Passasjerer")
    resultat = (inputkm * atNormKmM) + (inputtid * atNormTid) + (inputkmover * atNormKmOverM) + atNormStartM + inputtillegg
    if resultat < atNormMinstM:
        resultat = atNormMinstM
    print("{},- kroner\n".format(int(resultat)))

    print("9-16 Passasjerer")
    resultat = (inputkm * atNormKmM) + (inputtid * atNormTid) + (inputkmover * atNormKmOverL) + atNormStartL + inputtillegg
    if resultat < atNormMinstL:
        resultat = atNormMinstL
    print("{},- kroner\n".format(int(resultat)))

    print("KVELD 20:00 - 06:00, OG HELGER")
    print("1-4 Passasjerer")
    resultat = (inputkm * atHelgKmS) + (inputtid * atHelgTid) + atHelgStartS + inputtillegg
    if resultat < atHelgMinstS:
        resultat = atHelgMinstS
    print("{},- kroner\n".format(int(resultat)))


    print("5-8 Passasjerer")
    print((inputkm * atHelgKmM) + (inputtid * atHelgTid) + (inputkmover * atHelgKmOverM) + inputtillegg, ",- kroner")
    print("9-16 Passasjerer")
    print((inputkm * atHelgKmL) + (inputtid * atHelgTid) + (inputkmover * atHelgKmOverL) + inputtillegg, ",- kroner")
    print()
    print("HELLIGDAGER")
    print("1-4 Passasjerer")
    print((inputkm * atHolyKmS) + (inputtid * atHolyTid) + inputtillegg, ",- kroner")
    print("5-8 Passasjerer")
    print((inputkm * atHolyKmM) + (inputtid * atHolyTid) + (inputkmover * atHolyKmOverM) + inputtillegg, ",- kroner")
    print("9-16 Passasjerer")
    print((inputkm * atHolyKmL) + (inputtid * atHolyTid) + (inputkmover * atHolyKmOverL) + inputtillegg, ",- kroner")
    print()
    print("Alle priser er inklusive moms")
    print()


while True:
    try:
        kminput = input("Antall kilometer: ")
        if kminput.lower() == "q" or kminput.lower() == "quit":
            break
        if len(kminput) == 0:
            kminput = 0

        mininput = input("Antall minutter: ")
        if mininput.lower() == "q" or mininput.lower() == "quit":
            break
        if len(mininput) == 0:
            mininput = 0

        over30input = input("Antall kilometer over 30 km (kun ved bussbestilling: ")
        if over30input.lower() == "q" or over30input.lower() == "quit":
            break
        if len(over30input) == 0:
            over30input = 0

        tilinput = input("Antall kroner i tillegg: ")
        if tilinput.lower() == "q" or tilinput.lower() == "quit":
            break
        if len(tilinput) == 0:
            tilinput = 0

        agderPris(int(kminput), int(mininput), int(over30input), int(tilinput))
    except ValueError:
        print("FEIL: Unngå og tast inn noe annet enn tall.\n")
    except ZeroDivisionError:
        print("You cannot divide anything by 0!")
