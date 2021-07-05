D = [0] * 31
E = [0] * 31
pares = 0
N = int(input())
while N > 0:
    N = N - 1
    numero, lado = input().split()
    numero = int(numero)
    if lado == 'E':
        E[numero-30] = E[numero-30] + 1
    else:
        D[numero-30] = D[numero-30] + 1

    if E[numero-30] and D[numero-30]:
        E[numero-30] = E[numero-30] - 1
        D[numero-30] = D[numero-30] - 1
        pares += 1
print(pares)