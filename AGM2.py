import time
from random import randint

#ne fait rien pour le moment
def main(tableauInitial,eleves):
	resultat = []
	tableauAppreciations = count_appreciations(tableauInitial)
	formation = []
	
	e1 = choix_eleve1(tableauAppreciations)
	secondEleves = trouver_eleves_a_associer(e1,tableauInitial)

	resultat = generer_formation(e1,secondEleves,formation,tableauInitial,resultat)

	return resultat

#fonction qui va generer une nouvelle formation à partir d'une formation originelle(on peut dire que c'est le noeud d'une branche)
def generer_formation(e1,secondEleves,formation,tableauInitial,res):
	for i in range(len(secondEleves)):
		formationI = copie(formation)
		eleve2 = secondEleves[i]
		formationI.append([e1,eleve2])
		#newTableau = del_from_tableauInit(e1,eleve2,tableauInitial) ne marche plus
		if (len(newTableau) == 0) : #On a tout parcouru
			res.append(formationI)
			#return res
		else :
			e3 = choix_eleve1(count_appreciations(newTableau))
			secondEleves4 = trouver_eleves_a_associer(e3,newTableau)
			generer_formation(e3,secondEleves4,formationI,newTableau,res)

	return res

#compte les appreciations recus par chaque eleve (ex: 0 TB, 1 B, 2 AB, 0 I, 0 P, 1 AR)
# --fonctionne bien-- #
def count_appreciations(tableauAppreciations) :
	nb_eleves_restants = len(tableauAppreciations)
	comptage = []
	for k in range(0,nb_eleves_restants):
		comptage.append([])
		for l in range(0,6):
			comptage[k].append(0)
	for i in range(0,nb_eleves_restants):
		for j in range(0,nb_eleves_restants):
			if (tableauAppreciations[j][i] == "TB") :
				comptage[i][0] += 1
			elif (tableauAppreciations[j][i] == "B") :
				comptage[i][1] += 1
			elif (tableauAppreciations[j][i] == "AB") :
				comptage[i][2] += 1
			elif (tableauAppreciations[j][i] == "P") :
				comptage[i][3] += 1
			elif (tableauAppreciations[j][i] == "I") :
				comptage[i][4] += 1
			elif (tableauAppreciations[j][i] == "AR") :
				comptage[i][5] += 1
	return comptage

"""
#defini qui a le minimum de bonnes mentions par mention
def min_bonne_mention(comptage,nb_eleves_restants,mention,eleve):
	minimum = 100
	for i in range(0,nb_eleves_restants):
		if (minimum > comptage[i][mention] and eleve[i] in eleve):
			minimum = comptage[i][mention]
	print("min_bonne_mention.minimum&mention:",minimum,mention)
	return minimum

#permet de verifier si on a des eleves qui ont le meme nombre de mention sur la mention observee
def verif_egalite_nb_mention(comptage,nb_eleves_restants,mention,minimum,eleve):
	eleves_mm_nb_mentions = []
	#j = 0
	for i in range(0,nb_eleves_restants):
		print(i)
		if ((minimum == comptage[i][mention])): #and eleve[i] in eleve):
			eleves_mm_nb_mentions.append(eleve[i])
			#j += 1
			print("verif_egalite_nb_mention.cpteleve:",eleves_mm_nb_mentions)
	return eleves_mm_nb_mentions   

#trouve le premier eleve
def trouver_eleve_x(comptage,tableauAppreciations,nb_eleves_restants,mention,eleves):
    minimum = min_bonne_mention(comptage,nb_eleves_restants,mention,eleves)
    eleves = verif_egalite_nb_mention(comptage,nb_eleves_restants,mention,minimum,eleves)
    print("eleves: len=",len(eleves),": ",eleves)
    if mention == 6 or len(eleves) == 1:
        return eleves[0]
    if len(eleves) > 1:
        mention += 1
        return trouver_eleve_x(comptage,tableauAppreciations,nb_eleves_restants,mention,eleves)
        time.sleep(0.1)
"""

# trouve le premier eleve (parmis les moins aimes) 
def choix_eleve1(tableauAppreciations,eleves):
	"""
	nb_eleves_restants = len(tableauAppreciations)
	comptage = count_appreciations(tableauAppreciations)
	trouver_eleve_x(comptage,tableauAppreciations,nb_eleves_restants,mention,eleves)
	"""
	nombre_eleves = len(eleves)
	tableau_compteur = count_appreciations(tableauAppreciations)
	eleves_restants = eleves
	i = 0

	#on parcours les mentions en verifiant qu'il ne reste pas un seul eleve (cas le plus simple)
	while ( i < 6 and len(tableau_compteur) > 1):
		minimum = tableau_compteur[0][i]
		j = 0
		#print("min:",minimum)
		while (j < nombre_eleves ):
			notChanged = True
			if (tableau_compteur[j][i] > minimum ):
				pre_res = del_from_tableaux(eleves_restants[j],eleves_restants,tableau_compteur)
				eleves_restants = pre_res[0]
				tableau_compteur = pre_res[1]
				#print("tableau_compteur du if:",tableau_compteur,minimum)
				nombre_eleves -= 1
				notChanged = False
			elif (tableau_compteur[j][i] < minimum) :
				minimum = tableau_compteur[j][i]
				j -= 1
				pre_res = del_from_tableaux(eleves_restants[j],eleves_restants,tableau_compteur)
				eleves_restants = pre_res[0]
				tableau_compteur = pre_res[1]
				#print("on a trouve un autre min dans le else",tableau_compteur,minimum)
				nombre_eleves -= 1
				notChanged = False
			
			j += 1
		if (i == 5  and notChanged): # on fait la meme chose mais on rentre aussi quand on est seul sur cette mention et qu'il reste au moins un autre eleve
			pre_res = del_from_tableaux(eleves_restants[0],eleves_restants,tableau_compteur)
			eleves_restants = pre_res[0]
			tableau_compteur = pre_res[1]
			nombre_eleves -= 1
		i += 1
	eleve_restant = eleves_restants[0]
	print('On a selectionne le premier eleve: ', eleve_restant)
	return eleve_restant

#trouve les eleves à associer a celui entre en parametre         TODO: suppr lui meme des eleves et liste au debut
def trouver_eleves_a_associer(e1,tableau,eleves):
	print("On cherche a associer un ou plusieurs eleves a", e1)
	second_eleves = []
	indice_e1 = find_indice_eleve(e1,eleves)
	attributions_e1 = tableau[indice_e1]
	notBest = True

	#On regarde ceux a qui e1 a mis TB
	liste_mention = ["TB","B","AB","P","I","AR"]
	m = 0
	while (notBest and m < 6):
		mention = liste_mention[m]
		i = 0
		while (i < len(eleves)):
			if attributions_e1[i] == mention :
				#on ajoute ceux qui ont mis TB, ou B, ou AB
				if ((verif_mention_par_indices(i,indice_e1,"TB",tableau) == True) or (verif_mention_par_indices(i,indice_e1,"B",tableau) == True) or (verif_mention_par_indices(i,indice_e1,"AB",tableau) == True)): #je met true pour la visibilite, cf Fiorio le sang
					second_eleves.append(eleves[i])
			i += 1
		if second_eleves != [] : #si on a reussi a trouver qq un :)
			notBest = False
		m += 1
	if (notBest and m == 6): #AR-AR general
		tmp = del_from_tableaux(e1,eleves,tableau)
		eleves2 = tmp[0]
		tableau2 = tmp[1]
		print("trouver2:",tableau2,eleves2)
		second_eleves.append(eleves2)
	print("On obtient une liste des second_eleves: ", second_eleves)	
	return second_eleves

#renvoie un booleen pour dire si oui ou non l'eleve 'a' a mis telle mention a l'eleve 'b'
def verif_mention_par_indices(a,b,mention,tableauInitial):
	if tableauInitial[a][b] == mention :
		return True
	else:
		return False

#supprime un element de sa liste
def del_from_liste(element,liste):
	liste.remove(element)

#supprime un eleve, cad supprime l'eleves de la liste 'eleves' et supprime son equivalent dans le tableau compteur
#renvoie une copie
def del_from_tableaux(e,elevesInit,tableauInit):
	eleves = copie(elevesInit)
	tableau = copie(tableauInit)
	indice = find_indice_eleve(e,eleves)
	del_from_liste(e,eleves)
	del tableau[indice]
	return [eleves,tableau]

#copie une liste dans un autre espace memoire
def copie(liste):
	f = []
	for i in range(len(liste)):
		f.append(liste[i])
	return f

#trouve l'indice d'un eleve
def find_indice_eleve(e,eleves):
	indice = -1
	notFound = True
	i = 0
	while ( i < len(eleves) and notFound ):
		if (e == eleves[i]):
			indice = i
			notFound = False 
		i += 1
	return indice

####################################

#permet de tester différentes fonctions
def testmain(tab,taille,eleves):
    print("---taille:",taille)
    print("---tableau: ",tab)
    print("---comptage:",count_appreciations(tab))
    print("on affiche le resultat:")
    #res = trouver_eleve_x(count_appreciations(tab),tab,taille,0,eleves)
    #print(res)
    return 0

#VARIABLES de test
eleves = [0,1,2,3]
elevesTest = ["albert1","bernard2","patrick3","alice4"]

tabTest = [[-1,"AR","B","AR"],["AR",-1,"B","AB"],["AB","AR",-1,"AR"],["AB","AR","B",-1]]
tailleTest = len(tabTest)

e1 = elevesTest[3]

#testmain(tabTest,tailleTest,eleves2)
print("---tableau:",tabTest)
print("---comptage:",count_appreciations(tabTest))
print("")

e1 = choix_eleve1(tabTest,elevesTest)

trouver_eleves_a_associer(e1,tabTest,elevesTest)