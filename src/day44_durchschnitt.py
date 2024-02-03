print("Durchschnittsrechner: ")
print("Für wie viele Zahlen willst du den Durchschnitt berechnen?")
anzahl = int(input("Gebe die Anzahl der Zahlen ein: !))
summe = 0
for i in range(anzahl):
    summe = summe + int(input("Gebe eine Zahl ein: "))

durchschnitt = summe / anzahl
print("Der Durschnitt ist:",durchschnitt)
