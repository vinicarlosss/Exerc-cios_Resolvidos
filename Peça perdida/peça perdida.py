def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n-1)

def somatoriob(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma


n = int(input())
lista = [int(numero) for numero in input().split()]

print(somatorio(n)-somatoriob(lista))








