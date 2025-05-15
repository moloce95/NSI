mot = input()

mot_min = mot.lower()

if 'ui' in mot_min:
    print('il y a ui')

print(len(mot_min))

nbr_car = len(mot_min)
if nbr_car > 5:
    print(mot_min[-4 :])

mot_fin = mot_min.replace('e','*')
print(mot_fin)