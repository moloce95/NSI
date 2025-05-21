def tri_insertion(liste):
    L = list(liste)            # On fait une copie de la liste pour ne pas modifier l'originale
    N = len(L)                 # On regarde la taille de la liste
    for n in range(1, N):      # On parcourt la liste à partir du 2ᵉ élément
        cle = L[n]             # On garde l'élément à insérer dans la variable "cle"
        j = n - 1              
        while j >= 0 and L[j] > cle:  # On compare "cle" avec les éléments à gauche
            L[j + 1] = L[j]    # On décale l'élément vers la droite
            j = j - 1          # On recule d'une position pour continuer à comparer
        L[j + 1] = cle         # On insère "cle" à la bonne position
    return L                
# testons le
ma_liste = [14, 28, 12, 7, 55, 25]
print(tri_insertion(ma_liste))  # Affiche la liste triée
