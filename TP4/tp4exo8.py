dict = {"firstname": "yann", "name": "blanck", "promo": "RT 2022/2025", "group": "RT121" }

print("votre nom est %s ,prenom est %s, vous faites partie de la promo %s et votre groupe est %s" % (dict["name"], dict["firstname"], dict["promo"], dict["group"]))

############################################

print("les clés du dictionnaire sont:")
for x in dict.keys():
  print(f"-{x}")

print("les valeurs du dictionnaire sont:")
for x in dict.values():
  print(f"-{x}")

print("les tuplets du dictionnaire sont:")
for x in dict.items():
  print(f"-{x}")

#############################################

dict2 = {"firstname": "thibaut", "name": "cosenza", "promo": "RT 2022/2025", "group": "RT121" }

##############################################
binome = { 1 : dict, 2: dict2}

print("Les étudiants formants le binôme sont:")
for x in binome:
    print("- l'étudiant %s %s du groupe %s" % (binome[x]["name"], binome[x]["firstname"],binome[x]["group"]))
