from time import sleep

n = int(input("entrer un valeur positive: "))

for i in range(n+1):
    sleep(0.2)
    print(n)
    n=n-1