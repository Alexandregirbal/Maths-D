#permet de lister toutes les couples possibles pour un nombre entier n
def listeDeux(n):
    listeResultat=[]
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            listeResultat.append([i,j])
    return listeResultat

#permet de lister toutes les triplets possibles pour un nombre entier n
def listeTrois(n):
    listeResultat=[]
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            for k in range(j+1,n+1,1):
                listeResultat.append([i,j,k])
    return listeResultat

#prend une liste en argument
def liste3(liste):
    listeResultat=[]
    n = len(liste)
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            for k in range(j+1,n+1,1):
                listeResultat.append([liste[i-1],liste[j-1],liste[k-1]])
    return listeResultat

#pareil
def liste2(liste):
    listeResultat=[]
    n = len(liste)
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            listeResultat.append([liste[i-1],liste[j-1]])
    return listeResultat

#enumeration() enumere toutes les possibilités de groupes en connaissant le nombre de doublets et de triplets
def enumeration(triplet,doublet,dbt,elements,enum):

    if ((doublet < 0) or (triplet < 0)):
        return ([])

    if triplet>0 :
        t = triplet-1
        d = doublet
        perm = liste3(elements)
        for i in range(len(perm)):
            #print("FORt: ",i)
            tmp = [l for l in dbt]
            tmp.append(perm[i])
            diff = [k for k in elements]
            diff.remove(perm[i][0])
            diff.remove(perm[i][1])
            diff.remove(perm[i][2])
            #print(tmp)
            #print("Il reste :",diff)
            enumeration(t,d,tmp,diff,enum)
    elif doublet>0 :
        t = triplet
        d = doublet-1
        perm = liste2(elements)
        for j in range(len(perm)):
            tmp = [l for l in dbt]
            #print("FORd: ",j)
            #print("perm[j]: ", perm[j])
            tmp.append(perm[j])
            #print("tmp:",tmp)
            diff = [k for k in elements]
            diff.remove(perm[j][0])
            diff.remove(perm[j][1])
            #print("Il reste :",diff)
            enumeration(t,d,tmp,diff,enum)
        
    elif (triplet==0) and (doublet==0):    
        enum.append(dbt)
        print("On a fini un set de groupes\n")
        
    #print(enum)
    return (enum)

def main():
    '''
    n = int(input("Calculer les permutations possibles pour: "))    
    print(" Permutations de doublets: - -   ", listeDeux(n),"\n")
    print(" Permutations de triplets: - - - ", listeTrois(n),"\n")
    print(" avec une liste: ", liste2(["Alex","David","Paola","Jerem","Hugo","Audrey"]))
    '''
    d = int(input("Calculer les groupes avec ce nombre de doublets: "))
    t = int(input("Calculer les groupes avec ce nombre de triplets: "))
    print("\n")
    
    listFull = []   #liste qui sera fournie en param d'enum
    taille = 2*d + 3*t
    for i in range(1,taille+1):
        listFull.append(i)
    dbt = []
    print (listFull)    
    print (enumeration(t,d,dbt,listFull,[]))

# Et c'est partie !

main()
