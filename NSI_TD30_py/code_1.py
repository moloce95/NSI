matrice = []
matrice = [[0] * 5]

for i in range(4):  
    matrice.append([0] * 5)  

matrice[1][1]= 255
matrice[1][3]= 255
matrice[2][0]= 255
matrice[2][4]= 255
matrice[3][1]= 255
matrice[3][2]= 255
matrice[3][3]= 255
print(matrice)