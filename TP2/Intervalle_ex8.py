""""
x =  float(input("Entrez un nombre décimal : "))

if x >= 2 and x < 3 or x >0 and x <= 1 or x>= -10 and x<=-2:
    print(f"{x} appartient à I")
else:
    print(f"{x} n'appartient pas à I")

"""

x =  float(input("Entrez un nombre décimal : "))

if not(x<2) and x<3 or x>0 and not(x>1) or not(x<-10) and not(x>-2):

    print(f"{x} appartient à I")
else:
    print(f"{x} n'appartient pas à I")

