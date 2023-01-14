heur = 0
argent = 0

heur = int(input("entre le nombre d'heure: "))
argent = int(input("entre votre salaire: "))


if heur <= 160:
    salaire = heur * argent

elif heur >= 161 and heur <= 200:
    surplus = (heur - 160) * (argent * 1.25)
    salaire = (160 * argent + surplus)

elif heur >= 201:
    surplus2 = (heur - 200) * (argent * 1.25)
    surplus = 39 * argent * 1.25
    salaire = (160 * argent) + surplus +surplus2


print(salaire)


