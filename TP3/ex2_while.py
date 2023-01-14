from time import sleep

n = int(input("entrer un valeur positive: "))

while n >= 0:
    sleep(0.2)
    print(n)
    n=n-1

