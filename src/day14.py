import random
print("Spiele Schere-Stein-Papier gegen einen Computer!")
eingabe = input("Wähle aus: Schere (s), Stein (r) oder Papier (p)")
spielzuege = ["s", "p", "r"]
if eingabe in spielzuege:
    random.shuffle(spielzuege)
    computer = spielzuege[0]
    print("Computer: " + computer)

    if computer == eingabe:
        print("Unentschieden")
    elif computer == "s" and eingabe == "p":
        print("Du hast verloren!")
    elif computer == "r" and eingabe == "s":
        print("Du hast verloren!")
    elif computer == "p" and eingabe == "r":
        print("Du hast verloren!")
    elif computer == "s" and eingabe == "r":
        print("Du hast gewonnen!")
    elif computer == "r" and eingabe == "p":
        print("Du hast gewonnen!")
    elif computer == "p" and eingabe == "s":
        print("Du hast gewonnen!")
else:
    print("Falsche Eingabe!")
