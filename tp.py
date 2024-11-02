def saisir_tableau(longueur, nom_tableau):
    tableau = []
    for i in range(longueur):
        valeur = int(input(f"Entrez la valeur {i+1} pour le tableau {nom_tableau}: "))
        tableau.append(valeur)
    return tableau
def additionner_tableaux(tableau1, tableau2):
    tableau_somme = []
    for i in range(len(tableau1)):
        tableau_somme.append(tableau1[i] + tableau2[i])
    return tableau_somme
longueur = int(input("Entrez la longueur des tableaux: "))
tableau1 = saisir_tableau(longueur, "1")
tableau2 = saisir_tableau(longueur, "2")
tableau_somme = additionner_tableaux(tableau1, tableau2)
print("Tableau résultant de la somme : ", tableau_somme)
