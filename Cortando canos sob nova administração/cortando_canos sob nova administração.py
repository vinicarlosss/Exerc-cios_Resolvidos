def f_max(a, b):
    if a > b:
        return a
    else:
        return b

def result(i, n, t, comp_e_val):
    if (i == n):
        return 0
    elif (t == 0):
        return 0
    elif (t < 0):
        return -1

    return f_max(result(i + 1, n, t, comp_e_val), comp_e_val[i][1] + result(i, n, t - comp_e_val[i][0], comp_e_val))


numero, tamanho = list(map(int, input().split(" ")))
numero = int(numero)
comprimento_e_valor = []
for i in range(numero):
    k = tuple(map(int, input().split(" ")))
    comprimento_e_valor.append(k)

print(result(0, numero, tamanho, comprimento_e_valor))
