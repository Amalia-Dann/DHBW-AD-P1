# Berechnet den Preis für die Karten
# Bei 3 oder mehr Karten bekommt man 20% Rabatt
print("Berechnung des Preises für die Karten")
anzahl = int(input("Anzahl der gewünschten Karten: "))
betrag = anzahl * 15
if anzahl >= 3: 
    betrag = int(betrag * 0.8)
print("Der Preis für die Karten beträgt:" , betrag)
