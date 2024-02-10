def multiplikationstabelle():
    print("  |", end="")
    for i in range(10):
        print(f"{i:4}", end="")
    print("\n-----------------------------------------------")

    for i in range(10):
        print(f"{i} |", end="")
        for j in range(11):
            ergebnis = i * j
            print(f"{ergebnis:4}", end="")
        print()

multiplikationstabelle()
