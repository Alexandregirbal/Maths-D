#permet de lister toutes les doublets possibles pour un nombre entier n
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

#prend une liste en argument et renvoie tous les triplets poossibles
def liste3(liste):
    listeResultat=[]
    n = len(liste)
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            for k in range(j+1,n+1,1):
                listeResultat.append([liste[i-1],liste[j-1],liste[k-1]])
    return listeResultat

#pareil avec les doublets 
def liste2(liste):
    listeResultat=[]
    n = len(liste)
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            listeResultat.append([liste[i-1],liste[j-1]])
    return listeResultat
    
#github Luca
def estDoublon(solution, listeSolutions):
    if(len(listeSolutions) == 0):
        return False

    for solutionTest in listeSolutions:

        nb = 0

        i = 0
        while (i < len(solution)):
            correspondance = False
            for groupeSolTest in solutionTest:
                if (solution[i] == groupeSolTest):
                    nb += 1
                    correspondance = True

            if (correspondance == False):
                break

            i += 1

        if(nb == len(solution)):
            print(solution,"=",solutionTest)
            return True

    return False

#les groupes doivent etre ordonnes de la meme facon (1,2 et pas 2,1)
def listesEgales(a,b):
    i = 0
    lena = len(a)
    lenb = len(b)
    res = 0
    if (lena != lenb):
        return False 
    while (i < lena):
        j = 0
        while (j < lenb):
            if (a[i] == b[j]):
                res+=1
            j+=1
        i+=1
    if (res == lena):
        return True

def suppressionDoublons(liste):
    i = 0
    leng = len(liste)
    unicite = True
    while (i < leng):
        toCheck = liste[i]
        j = i+1
        while ((j < leng)):
            if (listesEgales(toCheck,liste[j])):
                print("Doublon trouve en position: ",j,". On supprime ",liste[j])
                #print(type([[]]))
                del liste[j]
                unicite = False
                leng = len(liste)
            j+=1
        i+=1
    print("Test unicite: ",unicite) #affiche true si il n'y a pas eu de doublons
    return liste

#genere une liste de couples (triplet,doublet) possibles pour un nombre donne n     
def generateTD(n):
    res = []
    if (n<2):
        return (res)
    elif (n == 2):
        return ([0,1])
    elif (n == 3):
        return([1,0])
    else:
        for i in range((n+2)//2): #pas besoin d'aller plus loin
            for j in range((n+2)//2):
                tmp = 3*i + 2*j
                if (tmp == n):
                    res.append([i,j])
        return res

def arrondiSup(n):
    res = n
    for i in range(n+1):
        if ((i<n) and (i+1>n)):
            res = i+1
    return res
    
def arrondiInf(n):
    res = n
    for i in range(n+1):
        if ((i<n) and (i+1>n)):
            res = i
    return res
        
#enumeration() enumere toutes les possibilites de groupes en connaissant le nombre de doublets et de triplets
def enumeration(triplet,doublet,dbt,elements,enum):

    if ((doublet < 0) or (triplet < 0)):
        return ([])

    if triplet>0 :
        t = triplet-1
        d = doublet
        perm = liste3(elements)
        borne = len(perm)
        if triplet > 1:
            borne = arrondiInf(len(perm)//2)
        for i in range(borne):
            tmp = [l for l in dbt] #besoin de faire une copie sans lien
            tmp.append(perm[i])
            diff = [k for k in elements]
            diff.remove(perm[i][0])
            diff.remove(perm[i][1])
            diff.remove(perm[i][2])

            enumeration(t,d,tmp,diff,enum)
    elif doublet>0 :
        t = triplet
        d = doublet-1
        perm = liste2(elements)
        borne = len(perm)//doublet
        for j in range(borne):
            tmp = [l for l in dbt]
            tmp.append(perm[j])
            diff = [k for k in elements]
            diff.remove(perm[j][0])
            diff.remove(perm[j][1])

            enumeration(t,d,tmp,diff,enum)
        
    elif (triplet==0) and (doublet==0):    
        enum.append(dbt)
        
    return (enum)
    
def enumDoublets(doublet,dbt,elements,enum):

    if (doublet < 0):
        return ([])

    elif doublet>0 : 
        d = doublet-1
        perm = liste2(elements)
        borne = len(perm)//doublet
        for j in range(borne):
            tmp = [l for l in dbt]
            tmp.append(perm[j])
            diff = [k for k in elements]
            diff.remove(perm[j][0])
            diff.remove(perm[j][1])

            enumDoublets(d,tmp,diff,enum)
        
    elif (doublet==0):    
        enum.append(dbt)
        
    return (enum)
    
def enumTriplets(triplet,dbt,elements,enum):

    if (triplet < 0):
        return ([])

    elif triplet>0 : 
        t = triplet-1
        perm = liste3(elements)
        borne = len(perm)//triplet
        for j in range(borne):
            tmp = [l for l in dbt]
            tmp.append(perm[j])
            diff = [k for k in elements]
            diff.remove(perm[j][0])
            diff.remove(perm[j][1])
            diff.remove(perm[j][2])

            enumTriplets(t,tmp,diff,enum)
        
    elif (triplet==0):    
        enum.append(dbt)
        
    return (enum)

#Pour tester les fonctions
def test():
    d = int(input("Calculer les groupes avec ce nombre de doublets: "))
    t = int(input("Calculer les groupes avec ce nombre de triplets: "))
    print("\n")
    
    testNum = []
    taille = 2*d + 3*t
    for i in range(1,taille+1):
        testNum.append(i)
        
    dbt = []    
    res = enumeration(t,d,dbt,testNum,[])
    print ("Nombre de groupes: ",len(res))
    print(res)
    
    test = [[[1,2],[4,5]],[[4,5],[1,2]]]
    print(suppressionDoublons(test))

#Prend en param la liste des elements a classer en groupes
#Renvoie tous les groupes possibles selon toutes les combinaisons possibles    
def main(elements):
    sum = 0
    t = len(elements)
    lTD = generateTD(t) # la liste generee des triplets et doublets possibles
    for i in range(len(lTD)):
        t = lTD[i][0]
        d = lTD[i][1]
        res = enumeration(t,d,[],elements,[])
        resU = suppressionDoublons(res)
        size = len(resU)
        print ("Nombre de groupes ayant ",t,"triplet(s) et ",d," doublet(s): ",size)
        sum += size
    print("\nNombre total de groupes: ", sum)
    
def main2(elements):
    d = len(elements)//2
    res = enumeration(0,d,[],elements,[])
    size = len(res)
    print ("Nombre de groupes ayant ",d," doublet(s): ",size)
    print(suppressionDoublons(res))

def main3(elements):
    t = len(elements)//3
    res = enumeration(t,0,[],elements,[])
    size = len(res)
    print ("Nombre de groupes ayant ",t," triplet(s): ",size)
    print(res)
    
####################################################    
#let's go hunt
test1 = [1,2,3,4,5,6]
test2 = [1,2,3,4,5,6,7,8]
testL = ["a","b","c","d","e","f"]
main(test2)
#main3(test2)
#print(liste2(test1))
#resD = enumDoublets(4,[],test2,[])
#resT = enumTriplets(2,[],test1,[]))
#print(len(resD),resD)
#print(len(resT),resT)
