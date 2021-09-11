import random
suma = 0
n = 1.0
m = 8
for i in range(0, m):
    for j in range(0, int(n)):
        suma = suma + random.randint(0, 1)
        res = suma/n
    #print n
    n = n*10
    print(res)
    suma = 0