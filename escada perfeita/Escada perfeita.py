soma = 0
movimento_cubo = 0
move_cubo = 0

n = int(input())
sequencia = [int(numero) for numero in input().split()]

for e in range(n):

    soma += sequencia[e]

ultima_fileira = int((((2*soma)/n) + (n-1))/2)
primeira_fileira = int(1 + ultima_fileira - n)

for e in range(n):

    move_cubo += (sequencia[e]-(e+primeira_fileira))
    if(sequencia[e]>e+primeira_fileira):
        movimento_cubo += (sequencia[e] - (e+primeira_fileira))
if move_cubo != 0:
    print("-1")

else:
    print(int(movimento_cubo))