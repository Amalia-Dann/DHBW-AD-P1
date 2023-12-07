from random import randint
n = randint(1,20)#
anzahlVersuche = 0
print("Ich habe mir eine Zahl von 1-100 ausgedacht.")
versuch = int(input("Rate meine Zahl: "))
anzahlVersuche = anzahlVersuche + 1

while (versuch != n) and (anzahlVersuche <= 10): # Solange nicht die richtige Zahl erraten wurde und nicht die maximale Anzahl an Versuchen gemacht wurde

    if (versuch < n) : # Wenn die Zahl kleiner ist als die gedachte Zahl
        print("Die gedachte Zahl ist größer!")
        anzahlVersuche = anzahlVersuche + 1
        versuch = int(input('Rate meine Zahl: '))
    else: # Wenn die Zahl größer ist als die gedachte Zahl
        print("Die gedachte Zahl ist kleiner!")
        anzahlVersuche = anzahlVersuche + 1
        versuch = int(input('Rate meine Zahl: '))

print("Richtig! Ich habe mir %d gedacht." % n) # Ausgabe bei richtiger Zahl
