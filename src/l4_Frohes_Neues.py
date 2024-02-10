from datetime import date
aktuellesDatum = date.today()
print("Das heutige Datum:", aktuellesDatum)
neujahr24 = date(2024, 1, 1)
if aktuellesDatum == neujahr24:
    print("Frohes neues Jahr 2024!")
else:
    print("Heute ist nicht Neujahr!")
