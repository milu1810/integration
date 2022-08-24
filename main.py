import ipaddress
import pandas as pd
import matplotlib.pyplot as plt
import graphviz as gr




                            # FUNCTION

#calcule le net mask selon le nombre d'hote voulu | CALCULATION OF THE MASK WITH THE NUMBER OF HOST THE USER WANT
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
    elif nbr < 65536 and nbr >= 32768:
        return(16)
    elif nbr < 131072 and nbr >= 65536:
        return(15)
    elif nbr < 262144 and nbr >= 131072:
        return(14)
    elif nbr < 524288 and nbr >= 262144:
        return(13)
    elif nbr < 1048576 and nbr >= 524288:
        return(12)
    elif nbr < 2097152 and nbr >= 1048576:
        return(11)
    elif nbr < 4194304 and nbr >= 2097152:
        return(10)
    elif nbr < 8388608 and nbr >= 4194304:
        return(9)
    elif nbr < 16777216 and nbr >= 8388608:
        return(8)
    elif nbr < 33554432 and nbr >= 16777216:
        return(7)
    elif nbr < 67108864 and nbr >= 33554432:
        return(6)
    elif nbr < 134217728 and nbr >= 67108864:
        return(5)
    elif nbr < 268435456 and nbr >= 134217728:
        return(4)
    elif nbr < 536870912 and nbr >= 268435456:
        return(3)
    elif nbr < 1073741824 and nbr >= 536870912:
        return(2)

#Permet d'additionner l'adresse par le nombre d'hote disponible selon le mask | ADD THE NUMBER OF HOST GIVEN BY THE MASK IN THE BASE ADDRESS
def additionreseau (address,nbrhote):
    return address+nbrhote


#permet de donner le nombre d'hote disponible selon le net mask | GIVE THE NUMBER OF HOST WITH THE HELP OF MASK
def nombrehotealloue(nn):
    netmask = 32
    nombrehote = 1
    while nn != netmask:
        netmask = netmask-1
        nombrehote = nombrehote*2
    return nombrehote




                            #CALCULE DE L ADDRESSE RESEAU|CALCULATION OF THE NETWORK ADDRESS
print('Veuillez entre l adresse')
adressedebase = ipaddress.ip_interface(input())
networ = adressedebase.network
print('l adresse de reseau est',networ)
print('le nombre d hote disponible est de', networ.num_addresses)
nbrmaxhote = networ.num_addresses
print('Veuillez entrez le nombre de sous reseau souhaitez')
nbrdereseau = int(input())
adresseprovi = adressedebase


#Creation des listes pour le DATA | LIST FOR MY DATAFRAME LATER
lstnmbhote = []
lstcalmaskres = []
lstadresse = []
lstnbrhotedispo = []

# Boucle qui permet de repeter les fonctions selon le nombre de sous réseau voulu | LOOP FOR CALCULATION WITH THE NUMBER OF SUB-NETWORK THE USER WANT
for x in range (nbrdereseau):
    print('nombre hote')
    nombrehotevoulu = int(input())
    lstnmbhote.append(nombrehotevoulu)
    print(nombrehotevoulu)
    lstcalmaskres.append(calmaskres(nombrehotevoulu))
    print(calmaskres(nombrehotevoulu))
    adresseprovi = additionreseau(adresseprovi,nombrehotealloue(calmaskres(nombrehotevoulu)))
    adresse_ip = str(adresseprovi)
    adresse_ip = adresse_ip[:-3]
    lstadresse.append(adresse_ip)
    print(adresse_ip)
    lstnbrhotedispo.append(nombrehotealloue(calmaskres(nombrehotevoulu)))
    print(nombrehotealloue(calmaskres(nombrehotevoulu)))


#Creation du data à utiliser pour créer le tableau | CREATION OF DATA FOR MY DATAFRAME
data = {'Nombre hote voulu':lstnmbhote,
        'Mask':lstcalmaskres,
        'adresse':lstadresse,
        'nombre hote dispo':lstnbrhotedispo}

data2 = [lstnmbhote, lstcalmaskres, lstadresse, lstnbrhotedispo]



#Creation du DATAFRAME | CREATE THE DATAFRAME
df = pd.DataFrame(data, columns=["Nombre hote voulu","Mask","adresse","nombre hote dispo"]).set_index("Nombre hote voulu")


#Triage du DATAFRAME | SORT THE DATAFRAME
df.sort_values(by=["Nombre hote voulu"], inplace=True)




#MONTRER LE DATAFRAME | SHOW THE DATAFRAME
print(df)

#Diagramme Circulaire | PLOT PIE

lstnbrhotedispo.append(nbrmaxhote)
lstadresse.append(adressedebase)
plt.pie(lstnbrhotedispo, labels=lstadresse)
plt.legend(lstnbrhotedispo)
plt.show()


                                #GRAPH
dot = gr.Digraph(comment='reseaux')
dot.node('A', str(nbrmaxhote))

#Boucle qui permet de créer des sommets ainsi que les connecter a mon adresse de base | LOOP HOW CREATE THE GRAPH WITH MY NUMBER OF HOST FOR EACH SUB-NETWORK
for index, columns in df.iterrows():
    dot.edge(str(columns["nombre hote dispo"]), str('A'), label='')

#sauvegarder mon résultat dans un fichier png | SAVING MY GRAPH IN A FILE.PNG
dot.format = 'png'
dot.render('my_graph', view=False)

