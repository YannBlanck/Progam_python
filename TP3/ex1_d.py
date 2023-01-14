
add= 0
i=0
x=0
while x<=1:
    x = int(input("entrer une valuer: "))


while add !=x:
    add = add+i

    if add>x:
        print("il n'y a pas de solution")
        break
    elif add == x:
        print(f"le nombre rechercher est {i} pour la valeur {x} ")

    else:
        i = i + 1
