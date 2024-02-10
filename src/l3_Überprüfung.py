print("Ich prüfe ob das eingegebenen Land zum Vereinigten Königreich gehört")
orte = ["England", "Wales", "Schottland", "Nordirland"
        ]
land = input("Gib das gewünschte Land ein: ")
if land in orte:
    print("Das Land", land, "gehört zum Vereinigten Königreich.")
else:
    print("Das Land", land, "gehört nicht zum Vereinigten Königreich.")
