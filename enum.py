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
def enumeration(doublet,triplet,elements):

    if ((doublet < 0) or (triplet < 0)):
        return ([])

    enum = []

    for i in range(0,doublet + triplet):
        if (triplet > 0):
            perm = liste3(elements)
            for i in range(len(perm)-1):
                diff = elements
                diff.remove(perm[i][0])
                diff.remove(perm[i][1])
                diff.remove(perm[i][2])
                print(elements)
                print(diff)
                triplet -= 1
                enumeration(doublet,triplet,diff)
        elif (doublet > 1):
            perm = liste2(elements)
            for i in range(len(perm)-1):
                diff = elements
                diff.remove(perm[i][0])
                diff.remove(perm[i][1])
                print(elements)
                doublet -= 1
                enumeration(doublet,triplet,diff)
        else:   #cas où doublets = 0 ou quand on arrive à doublet == 1 et on a deja traité les triplets
            enum.append(elements)
        
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
    
    listFull = []   #liste qui sera fournie en param d'enum
    taille = 2*d + 3*t
    for i in range(1,taille+1):
        listFull.append(i)
    print (listFull)    
    print (enumeration(d,t,listFull))

# Et c'est partie !

main()
