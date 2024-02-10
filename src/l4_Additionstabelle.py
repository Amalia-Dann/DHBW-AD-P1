def additionstabelle(n):
    print("Additionstabelle für", n, ":\n")


    print(" +  |", end="")
    for i in range(1, n + 1):
        print(f" {i:2}", end="")
    print("\n----+" + "---" * n)


    for i in range(1, n + 1):
        print(f" {i:2} |", end="")
        for j in range(1, n + 1):
            result = i + j
            print(f" {result:2}", end="")
        print()


additionstabelle(10)
