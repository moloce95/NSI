n = int(input('Mettre nombre'))
d = []
f = 1
e = 1
for x in range(n):
    d.append(f)
    d.append(e)
    f = f + 1
    e = e + 1
print(d)