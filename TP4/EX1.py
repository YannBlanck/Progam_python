table=[]

valeur = float(input("entrer la valeur a multiplier"))


for i in range(10):
    result = valeur*i
    table.append(round(result,2))

i=0

for i in range(10):
    print(f"{valeur} * {i} = {table[i]}")