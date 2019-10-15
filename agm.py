import time
#compte le nombre de mention par eleve --> renvoie le tableau du nombre de mention reçue des eleve par mention
def compter_mention(tableau_preference,nb_eleves_restants):
    comptage = []
    for i in range(0,nb_eleves_restants):
        comptage.append([])
        for j in range(0,6):
            comptage[i].append(0)
    for i in range(0,nb_eleves_restants):
        for j in range(0,nb_eleves_restants):
            #print (comptage)
            if (tableau_preference[i][j] == "TB") :
                comptage[i][0] += 1
            elif (tableau_preference[i][j] == "B") :
                comptage[i][1] += 1
            elif (tableau_preference[i][j] == "AB") :
                comptage[i][2] += 1
            elif (tableau_preference[i][j] == "P") :
                comptage[i][3] += 1
            elif (tableau_preference[i][j] == "I") :
                comptage[i][4] += 1
            elif (tableau_preference[i][j] == "AR") :
                comptage[i][5] += 1
    return comptage

def min_bonne_mention(comptage,nb_eleves_restants,mention,eleve):
    minimum = 100
    for i in range(0,nb_eleves_restants):
        if (minimum > comptage[i][mention] and i in eleve):
            minimum = comptage[i][mention]
    print("min: ",minimum)
    return minimum

#permet de verifier si on a des eleves qui ont le meme nombre de mention sur la mention observée
def verif_egalite_nb_mention(comptage,nb_eleves_restants,mention,minimum,eleve):
    cpt_eleve = []
    j = 0
    for i in range(0,nb_eleves_restants):
        if ((minimum == comptage[i][mention]) and i in eleve):
            cpt_eleve.append(0)
            cpt_eleve[j] = i
            j += 1
    print("cpt_eleve: ",cpt_eleve)
    return cpt_eleve

        

#trouve le premier élève
def trouver_eleve_x(comptage,tableau_preference,nb_eleves_restants,mention,eleve):
    res = -1
    if mention == 5:
        return eleve[0]
    minimum = min_bonne_mention(comptage,nb_eleves_restants,mention,eleve)
    eleve = verif_egalite_nb_mention(comptage,nb_eleves_restants,mention,minimum,eleve)
    print(len(eleve))
    if len(eleve) > 1:
        mention += 1
        trouver_eleve_x(comptage,tableau_preference,nb_eleves_restants,mention,eleve)
        time.sleep(2)
    else:
        res = eleve[0]
        print("eleve else 0:", res)
    print("eleve res 0:", res)
    return res


def main(tab,taille,eleves):
    print("taille: ",taille)
    #print("tab: ",tab)
    print(compter_mention(tab,taille))
    res = trouver_eleve_x(compter_mention(tab,taille),tab,taille,0,eleves)
    print(res)
    return 0
####################################
eleves = [0,1,2,3,4,5]
test = [[-1,"TB","B","P","AR","AB"],["B",-1,"B","P","B","AB"],["AB","TB",-1,"TB","B","B"],["B","B","AB",-1,"P","AR"],["I","TB","B","AB",-1,"P"],["P","AB","B","B","TB",-1]]
test2 = [[-1,"TB"],["TB",-1]]
t = len(test)
main(test,t,eleves)