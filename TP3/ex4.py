
n = int(input("entrer une valeur: "))

case = int(input("\nchoisir un type de boucle\n0:Boucle while\n1:Boucle For \n>:"))

fact = n
i=0


if case == 0:
    while i != n-1:
        i = i+1
        fact *= n-i

    print(f"le factoriel de {n} et {fact}")

elif case == 1:
    for i in range(n-1):
        fact *= n-(i+1)
    print(f"le factoriel de {n} et {fact}")

else:
    case = int(input("\nchoisir un type de boucle\n0:Boucle while\n1:Boucle For \n>:"))