L = []
i=0
N=0

N = int(input("entrer le nombre de valeur voulue: "))

for i in range(N):
    L.append(int(input(f"entrer la valeur {i}:")))

L.sort()
print(L)