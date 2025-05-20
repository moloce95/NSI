def tri_insertion(liste):
    # on commence par le deuxième élément
    for i in range(1,len(liste)):
        case_en_cours = liste[i] #mémorise la valeur de la case en cours
        j=i-1  # Indice de l'élément précédent
        while j >= 0 and case_en_cours < liste[j]:
            liste[j+1] = liste[j]  # Décale l'élément vers la droite
            j= j-1  # Passe à l'élément précédent
            liste[j+1] = case_en_cours  # Place la valeur à la bonne position
    return liste  # Retourne la liste triée

ma_liste = [18,12,22,7,55,25]  
a=tri_insertion(ma_liste)  
print(a)