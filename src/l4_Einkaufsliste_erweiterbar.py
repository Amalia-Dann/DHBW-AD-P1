loop= True
print("Dies ist eine Einkaufsliste: ")
liste = ["Äpfel", "Brot", "Salat"]
print(liste)
while loop == True:
  print("Möchtest du noch etwas hinzufügen")
  antwort =int(input("1: Ja; 2: Nein "))
  if antwort == 1:
    liste.append(input("Zur Liste hinzufügen: "))
    print("Dies ist die neue Einkaufsliste: ")
    print(liste)
  else:
    loop = False
