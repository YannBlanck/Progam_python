chaine = input("entrer une chaine de caractére: ")
chaine2 = ""
y = 0

for i in range(len(chaine)):
    v = chaine[i].isalpha()

    if v == True:
        chaine2 = chaine2 +chaine[i]


print(chaine)
print(chaine2)

chaine2 = chaine2.lower()

if chaine2 == chaine2[::-1]:
    print("palindrome")

else:
    print("pas palindrome")
