def gluecksrad():
    felder = ["Feld 1", "Feld 2", "Feld 3", "Feld 4", "Niete"]
    print("Dies ist ein GLücksrad!)

    gewaehltes_feld = random.choice(felder)

    print("Das Glücksrad wurde gedreht!")
    print("Es ist: " + gewaehltes_feld)

    if gewaehltes_feld == felder[0]:
        print("Herzlichen Glückwunsch, du hast ein Eis gewonnen!")
    elif gewaehltes_feld == felder[1]:
        print("Herzlichen Glückwunsch, du hast ein Stück Kuchen gewonnen!")
    elif gewaehltes_feld == felder[2]:
        print("Herzlichen Glückwunsch, du hast ein Plüschtier gewonnen!")
    elif gewaehltes_feld == felder[3]:
        print("Herzlichen Glückwunsch, du hast einen Gutschein gewonnen!")
    else:
        print("Leider ist es eine Niete. Du hast nichts gewonnen. Versuche es nochmal!")

gluecksrad()
