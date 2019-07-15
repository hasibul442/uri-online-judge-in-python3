A = (input())
B = (input())
C =(input())

if (A=="vertebrado"):
    if (B == "ave"):
        if (C=="carnivoro"):
            print("aguia")
        elif (C=="onivoro"):
            print("pomba")
    elif (B=="mamifero"):
        if (C=="onivoro"):
            print("homem")
        elif (C=="herbivoro"):
            print("vaca")
elif (A=="invertebrado"):
    if (B=="inseto"):
        if (C=="hematofago"):
            print("pulga")
        elif (C=="herbivoro"):
            print("lagarta")
    elif (B=="anelideo"):
        if (C=="hematofago"):
            print("sanguessuga")
        elif (C=="onivoro"):
            print("minhoca")
