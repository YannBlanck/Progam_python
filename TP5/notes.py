i=0
total = 0
coef = 0
resultat = 0

for i in range(5):
    note = input(f"Veuillez entrer la note du module {i} et le coefficient\ncorrespondant: ")

    x = note.split(" ")
    total = total + (float(x[0]) * float(x[1]))
    coef = coef + float(x[1])
    resultat = total / coef
    if float(x[0]) <8:
        print("non admis")
        break
    if i == 4:
        print(round(resultat, 2))

        if round(resultat, 2) > 10:
            print("admis")
            print(resultat)

        else:
            print("non admis")
            print(resultat)

