#soma os elementos da linha
def soma_linha(soma_linhas,quadrado):

    for i in range(n):
        soma_linha = 0
        for j in range(n):
            soma_linha += quadrado[i][j]
        soma_linhas.append(soma_linha)
    return(soma_linhas)

#soma os elementos da coluna
def soma_coluna(soma_colunas,quadrado):
    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna+= quadrado[i][j]
        soma_colunas.append(soma_coluna)
    return (soma_colunas)

#verifica qual linha e qual coluna possui o número diferente
def verifica_diferente(lista):
    chave = lista[0]
    chave_anterior = lista[0]
    for e in range(1,len(lista)):
        if chave != lista[e] and lista[e] != chave_anterior:
            chave_anterior = chave
            chave = lista[e]
        elif chave == lista[e] and chave != chave_anterior:
            chave = chave_anterior
            break
    return(lista.index(chave))

#encontra o numero original modificado por laura
def numero_original(lista,quadrado,linha,coluna):
    chave = lista[0]
    chave_anterior = lista[0]
    for e in range(1,len(lista)):
        if chave != lista[e] and lista[e] != chave_anterior:
            chave_anterior = chave
            chave = lista[e]
        elif chave == lista[e] and chave != chave_anterior:
            chave = chave_anterior
            break
    while True:
        try:
            if chave>lista[lista.index(chave)+1]:
                numero_original = quadrado[linha][coluna] - (chave-lista[lista.index(chave)+1])
                return (numero_original)
                break
            elif chave < lista[lista.index(chave) + 1]:
                numero_original = quadrado[linha][coluna] + (lista[lista.index(chave) + 1] - chave )
                return(numero_original)
                break
        except:
            if chave>lista[lista.index(chave)-1]:
                numero_original = quadrado[linha][coluna] - (chave-lista[lista.index(chave)+1])
                return(numero_original)
                break
            elif chave < lista[lista.index(chave) - 1]:
                numero_original = quadrado[linha][coluna] + (lista[lista.index(chave) + 1]- chave)
                return(numero_original)
                break



n = int(input())
soma_linhas = []
soma_colunas = []
quadrado = []

for e in range(n):
    quadrado.append(list(map(int,input().split())))


soma_linha(soma_linhas,quadrado),soma_coluna(soma_colunas,quadrado)

#posição que se encontra o número que laura modificou
linha = verifica_diferente(soma_linhas)
coluna = verifica_diferente(soma_colunas)

print(numero_original(soma_linhas,quadrado,linha,coluna),quadrado[linha][coluna])
