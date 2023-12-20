anzahl = int(input("Wie viele Zahlen soll die Zahlenfolge enthalten? "))

n1, n2 = 0, 1
count = 0

if anzahl <= 0:
   print("Bitte wähle eine positive Zahl!")

elif anzahl == 1:
   print("Fibonacci Reihe bis",anzahl,":")
   print(n1)
else:
   print("Fibonacci Reihe:")
   while count < anzahl:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
