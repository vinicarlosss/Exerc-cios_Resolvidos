def definemaior(x,y):

    if x > y:
        return x

    return y

l, c, m, n = [int(numero) for numero in input().split()]
fazenda = []

for i in range(l): #criação da matriz da fazenda de caju
    caju = list(map(int,input().split()))
    fazenda.append(caju)

T = [[0 for _ in range(c)] for _ in range(l)] #criação da matriz auxiliar

for i in range(l):
    for j in range(c):
        if i == 0 and j == 0:
            T[i][j] = fazenda[i][j]
        elif i == 0:
            T[i][j] = T[i][j-1] + fazenda[i][j]
        elif j == 0:
            T[i][j] = T[i-1][j] + fazenda[i][j]
        else:
            T[i][j] = fazenda[i][j]+T[i][j-1] + T[i-1][j] - T[i-1][j-1]

if l == m and c == n:
    print(T[m-1][n-1])

elif l == m and n < c:
    print(T[m-1][n-1])
else:
    maiorvalor = 0

    for i in range(l):
        for j in range(c):

            if i - m <0 and j == 0:
                resultado = T[i][j]
                maiorvalor = definemaior(resultado, maiorvalor)
            elif i-m > 0 and j-n < 0:
                resultado = T[i][j] - T[i-m][j]
                maiorvalor = definemaior(resultado, maiorvalor)

            elif i - m <0 and j-n < 0:
                resultado = T[i][j]
                maiorvalor = definemaior(resultado, maiorvalor)
            else:
                resultado = T[i][j] - T[i-m][j] - T[i][j-n] + T[i-m][j-n]
                maiorvalor = definemaior(resultado, maiorvalor)

    print(maiorvalor)