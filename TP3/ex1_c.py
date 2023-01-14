i = 0
x=0
a=0
b=0
c=0

while i<10:
    x = int(input("entrer la valeur entre 0 et 20 : "))
    if x>=0 and x<=20:


        if x<10:
            a=a+1
            i = i + 1
        elif x>=10 and x<15:
            b=b+1
            i = i + 1
        elif x>=15 and x<20:
            c=c+1
            i = i + 1



print(f" Le nombre de valeurs inférieur strictement à 10 est {a}")
print(f" Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est {b}")
print(f" Le nombre de valeurs supérieur ou égale à 15 est {c}")
