import math

print("Möchten Sie die Fläche oder den Umfang eines Kreises berechnen?")
auswahl = input("Geben Sie 'Fläche' oder 'Umfang' ein: ").lower()

if auswahl == 'fläche':
    radius = float(input("Geben Sie den Radius des Kreises ein: "))
    flaeche = math.pi * radius ** 2
    print(f"Die Fläche des Kreises mit Radius {radius} beträgt: {flaeche:.2f}")
elif auswahl == 'umfang':
    radius = float(input("Geben Sie den Radius des Kreises ein: "))
    umfang = 2 * math.pi * radius
    print(f"Der Umfang des Kreises mit Radius {radius} beträgt: {umfang:.2f}")
else:
    print("Ungültige Auswahl. Bitte geben Sie 'Fläche' oder 'Umfang' ein.")
