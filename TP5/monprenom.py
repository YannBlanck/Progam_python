#######################
nom1 = input("entrer votre nom: ")
prenom1 = input("entrer votre prenom: ")


#######################
nom2 = input("entrer votre nom: ")
prenom2 = input("entrer votre prenom: ")


if nom1<nom2:
    print(nom1.upper(), prenom1.capitalize())
    print(nom2.upper(), prenom2.capitalize())

elif nom1>nom2:
    print(nom2.upper(), prenom2.capitalize())
    print(nom1.upper(), prenom1.capitalize())

elif prenom1<prenom2:
    print(nom1.upper(), prenom1.capitalize())
    print(nom2.upper(), prenom2.capitalize())

else:
    print(nom2.upper(), prenom2.capitalize())
    print(nom1.upper(), prenom1.capitalize())

