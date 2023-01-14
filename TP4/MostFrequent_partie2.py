L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6,6,6,6]

i=0
nbr = 0
oldcnbr = 0
cnbr = 0 #nombre de foix ou l'on trouvre nrb
snbr = 0

for i in range(len(L1)):
    nbr = L1[i]

    cnbr = L1.count(L1[i])

    if oldcnbr < cnbr:
        snbr = nbr
        oldcnbr = cnbr

    cnbr = 0

print(f"Le nombre le plus frequent dans la liste est le : {snbr} ({oldcnbr} x)")






""""** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""