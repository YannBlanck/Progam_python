binome = ("yann", "thibaut")

print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

#################################
bi = list(binome)
bi[1] = input("changer le binome: ")
binome = tuple(bi)
print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

#########################

bi = list(binome)
del bi[1]
binome = tuple(bi)
print(binome)

###########################

binome = ("yann", "thibaut")
bi = list(binome)
bi.append( input("entre le nom de la troisième personne: "))
binome = tuple(bi)
print(binome)