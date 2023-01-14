import random

P = random.randint(0,100)
print(P)

if P>=0 and P<=50:
    print("Pile!")
elif P>=51 and P<=100:
    print("Face!")