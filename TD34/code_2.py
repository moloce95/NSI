n = int(input('Rentrée nombre:' ))
result = []
for i in range(1, n + 1):
    for j in range(1, i + 1):
        result.append(j)
print(result)