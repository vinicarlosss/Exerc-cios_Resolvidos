def maximovalor(i,tamanhomaximo,comprimentovalor,numero):
    if comprimentovalor[i][0] == tamanhomaximo:
        return comprimentovalor[i][1]
    resposta = 0
    tamanhoCorte = 0
    for e in range(numero):
        if (tamanhoCorte + comprimentovalor[i][0]) > tamanhomaximo:
            i += 1
            continue
        else:
            tamanhoCorte += comprimentovalor[i][0]
            resposta += comprimentovalor[i][1]
            i += 1
    return resposta


numero, tamanhoMaximo = [int(e) for e in input().split()]
comprimentoValor = []
for e in range(numero):
    pedido = tuple(map(int,input().split()))
    if pedido[0] > tamanhoMaximo:
        numero -= 1
        continue
    else:
        comprimentoValor.append(pedido)

print(maximovalor(0,tamanhoMaximo,comprimentoValor,numero))