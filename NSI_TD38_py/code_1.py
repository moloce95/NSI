import math # importe la bibliothèque math pour les calculs mathématiques
def racines(coef):
    a, b, c, = coef[0], coef[1], coef[2]
    delta = b**2 - 4 * a * c
    if delta<0:
        result = (0, )
    else: 
        if delta == 0:
            x = -b / (2 * a)
            result = (1, x)
        else:
            x1 = ( -b - math.sqrt(delta)) / (2 * a)
            x2 = ( -b + math.sqrt(delta)) / (2 * a)
            result = (2, x1, x2)
    return result