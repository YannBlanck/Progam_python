#exercice 4

BASE = 4

fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut : ")

nouvelleQuantite = fromage * nbConvives / BASE
print(f"- {nouvelleQuantite} gr de fromage ")
nouvelleQuantite = eau * nbConvives / BASE
print(f"- {nouvelleQuantite} dl d'eau")
nouvelleQuantite = ail * nbConvives / BASE
print(f"- {nouvelleQuantite} gousse(s) d'ail")
nouvelleQuantite = pain * nbConvives / BASE
print(f"- {nouvelleQuantite} gr de pain ")

