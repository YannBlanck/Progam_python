L = []
i=0
y=0
N=0
memoirei = 0
memoirey = 0
pos = 0
p=0

N = int(input("entrer le nombre de valeur voulue: "))

for i in range(N):
    L.append(int(input(f"entrer la valeur {i}:")))


i=0
for i in range(N):
    memoirey = L[i]
    print(L)

    while y != N:
        if L[y] < memoirey:
            memoirey = L[y]
            pos = y


        y = y+1

    memoirei = L[i]
    L[i] = memoirey
    L[pos] = memoirei
    p = p+1
    y=0
    y = p
    pos = y
