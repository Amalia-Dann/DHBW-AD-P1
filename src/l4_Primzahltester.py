zahl = int(input("Gib eine Zahl ein: "))

if zahl == 1:
    print(zahl, "ist keine Primzahl")
elif zahl > 1:
    for i in range(2, zahl):
        if (zahl % i) == 0:
            print(zahl, "ist keine Primzahl")
            print(i, "mal", zahl // i, "ist", zahl)
            break
    else:
        print(zahl, "ist eine Primzahl")

else:
    print(zahl, "ist keine Primzahl")
