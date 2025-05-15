scrabble = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 
            'G':2, 'H':4, 'I':1, 'J':8, 'K':5,}
somme = 0
mot = input("Entrez un mot : ")
mot = mot.upper()

for i in mot:
    somme = somme + int(scrabble.get(i))

print(somme)