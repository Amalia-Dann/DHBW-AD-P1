print("Dies ist ein Taschenrechner!")
print("A: Zwei Zahlen Addieren")
print("B: Zwei Zahlen Subtrahieren")
print("C: Zwei Zahlen Multiplizieren")
print("D: Zwei Zahlen Dividieren")

rechnung = input("Wähle aus: ")

zahl_1 = float(input("Erste Zahl: "))
zahl_2 = float(input("Zweite Zahl: "))
ergebnis = 0

if rechnung == "A":
    rechenzeichen = "+"
    ergebnis = zahl_1 + zahl_2
elif rechnung == "B":
    rechenzeichen = "-"
    ergebnis = zahl_1 - zahl_2
elif rechnung == "C":
    rechenzeichen = "*"
    ergebnis = zahl_1 * zahl_2
elif rechnung == "D":
    rechenzeichen = "/"
    ergebnis = zahl_1 / zahl_2
else:
    print("Error, diese Option gibt es nicht")

print("Das Ergebnis von", zahl_1, rechenzeichen, zahl_2, "ist", ergebnis)
