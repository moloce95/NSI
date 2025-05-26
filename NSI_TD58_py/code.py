def tri_selection(liste):
    # Parcourt la liste jusqu'à l'avant-dernier élément
    for i in range(len(liste) - 1):
        indice_du_min = i 
        # Parcourt le reste de la liste pour trouver le plus petit élément
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[indice_du_min]:  # Si on trouve plus petit
                indice_du_min = j  # On change l'indice du minimum
        if indice_du_min != i:  # Si un plus petit élément a été trouvé
            x = liste[indice_du_min]  # On assigne la valeur minimale à x
            liste[indice_du_min] = liste[i]
            liste[i] = x
    return liste

ma_liste = [18, 12, 22, 7, 55, 25] 
a = tri_selection(ma_liste)  
print(a) 