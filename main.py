import ipaddress
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


                            # PARTI FONCTION

#Calcule nombre hote Pas utiliser car problème de type
'''def calculhote (nbr):
    nbe = nbr.num_addresses
    return nbe'''

#calcule le net mask Pas utilser car problème de type
'''def DecMask(ne):
    return ne.netmask'''

#calcule le net mask selon le nombre d'hote voulu
def calmaskres (nbr):
    if nbr < 3:
        return(31)
    elif nbr < 8 and nbr >= 3:
        return 29
    elif nbr < 16 and nbr >= 8:
        return(28)
    elif nbr < 32 and nbr >= 16:
        return(27)
    elif nbr < 64 and nbr >= 32:
        return(26)
    elif nbr < 128 and nbr >= 64:
        return(25)
    elif nbr < 256 and nbr >= 128:
        return(24)
    elif nbr < 512 and nbr >= 256:
        return(23)
    elif nbr < 1024 and nbr >= 512:
        return(22)
    elif nbr < 2048 and nbr >= 1024:
        return(21)
    elif nbr < 4096 and nbr >= 2048:
        return(20)
    elif nbr < 8192 and nbr >= 4096:
        return(19)
    elif nbr < 16384 and nbr >= 8192:
        return(18)
    elif nbr < 32768 and nbr >= 16384:
        return(17)


#Permet d'additionner l'adresse par le nombre d'hote voulu
def additionreseau (address,nbrhote):
    return address+nbrhote


#permet de donner le nombre d'hote disponible selon le net mask
def nombrehotealloue(nn):
    if nn == 32:
        return 1
    elif nn == 31:
        return 2
    elif nn == 30:
        return 4
    elif nn == 29:
        return 8
    elif nn == 28:
        return 16
    elif nn == 27:
        return 32
    elif nn == 26:
        return 64
    elif nn == 25:
        return 128
    elif nn == 24:
        return 256
    elif nn == 23:
        return 512
    elif nn == 22:
        return 1024
    elif nn == 21:
        return 2048
    elif nn == 20:
        return 4096
    elif nn == 19:
        return 8192
    elif nn == 18:
        return 16384
    elif nn == 17:
        return 32768






                            #CALCULE DE L ADDRESSE RESEAU
print('Veuillez entre l adresse')
adressedebase = ipaddress.ip_interface(input())
networ = adressedebase.network
print('l adresse de reseau est',networ)
print('le nombre d hote disponible est de', networ.num_addresses)
nbrmaxhote = networ.num_addresses
print('Veuillez entrez le nombre de sous reseau souhaitez')
nbrdereseau = int(input())
adresseprovi = adressedebase



#Creation des listes pour le DATA
lstnmbhote = []
lstcalmaskres = []
lstadresse = []
lstnbrhotedispo = []


for x in range (nbrdereseau):
    print('nombre hote')
    nombrehotevoulu = int(input())
    lstnmbhote.append(nombrehotevoulu)
    print(nombrehotevoulu)
    lstcalmaskres.append(calmaskres(nombrehotevoulu))
    print(calmaskres(nombrehotevoulu))
    adresseprovi = additionreseau(adresseprovi,nombrehotealloue(calmaskres(nombrehotevoulu)))
    lstadresse.append(adresseprovi)
    print(adresseprovi)
    lstnbrhotedispo.append(nombrehotealloue(calmaskres(nombrehotevoulu)))
    print(nombrehotealloue(calmaskres(nombrehotevoulu)))



#Creation du data à utiliser pour créer le tableau
data = {'Nombre hote voulu':lstnmbhote,
        'Mask':lstcalmaskres,
        'adresse':lstadresse,
        'nombre hote dispo':lstnbrhotedispo}


#Creation du DATAFRAME
df = pd.DataFrame(data, columns=["Nombre hote voulu","Mask","adresse","nombre hote dispo"]).set_index("Nombre hote voulu")


#Triage du DATAFRAME
df.sort_values(by=["Nombre hote voulu"])

#MONTRER LE DATAFRAME
print(df)

#Diagramme Circulaire
plot = df.plot.pie(y='nombre hote dispo', figsize=(5,5))
plt.show()
