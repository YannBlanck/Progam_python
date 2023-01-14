nmax = 10 #taille max du vecteur

v1=[]
v2=[]
n=0
i=0
scal=0


while n<1 or n >= nmax:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

print("Saisie du premier vecteur : ")
while i !=n :
    v1.append(int(input(f"v1[{i}] = ")))
    i=i+1

i=0
print("Saisie du premier vecteur : ")
while i !=n :
    v2.append(int(input(f"v2[{i}] = ")))
    i=i+1

for i in range(n):
    scal = scal+(v1[i]*v2[i])

print(f"Le produit scalaire de v1 par v2 vaut {scal}")
