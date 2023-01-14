a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")


t = c
c = b
b = a
a = t


# a,b,c = c,a,b est une autre possibilité

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)


