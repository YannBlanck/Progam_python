
NBR = int(input("Entrez un nombre entier: "))

if NBR == 0:
    print("Le nombre est zéro (et il est pair)")

elif NBR%2 == 0:
    if NBR > 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est négatif et pair")

else:
    if NBR > 0:
        print("Le nombre est positif et impair")
    else:
        print("Le nombre est négatif et imppair")
