nom_prenom = input("Entrez vos noms et prénoms séparés par un espace :")
nom = nom_prenom.split() [0]
print(nom)

a = nom[0].upper()
print(a)
prenom = nom_prenom.split() [1]
b = prenom[0].upper()

print(a,b)