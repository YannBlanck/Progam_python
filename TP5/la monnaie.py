
argent =0
argent = int(input("entre l'argent que vous avez: "))
argent2 = argent

cent = 0
cinq = 0
dix = 0
deux = 0
un =0

cent = int(argent/100)
argent = argent%100
cinq = int(argent/50)
argent = argent%50
dix = int(argent/10)
argent = argent%10
deux = int(argent/2)
argent = argent%2
un = int(argent)

print(f"{argent2} euros, c'est donc {cent} billets de 100, {cinq} de 50, {dix} de 10,{deux} pièces de 2 et {un} pièces de 1 ")