class No:
    def __init__(self, dado=None):
        self._dado = dado
        self._prox = None



class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def isVazia(self):
        if self._inicio == None:
            return True
        return False

    def inserirNoFim(self, dado=None):
        novono = No(dado)
        if self.isVazia():
            self._inicio = self._fim = novono
        else:
            self._fim._prox = novono
            self._fim = novono

    def removerDoInicio(self):
        self._inicio = self._inicio._prox

    def mandaProFim(self):
        self.inserirNoFim(self._inicio._dado)
        self.removerDoInicio()


def isIgual(deckMesa, deckJogador):
    if deckJogador._inicio._dado == deckMesa._inicio._dado:
        return True
    return False


F = int(input())
festas = [0 for _ in range(F)]
jogadores = []
contador = 0
resultados = [0 for _ in range(F)]
while F > 0:
    F -= 1
    mesa = [int(numero) for numero in input().split()]
    cartasMesa = Fila()
    for i in mesa:
        cartasMesa.inserirNoFim(i)
    festas[contador] = cartasMesa
    jogadores.append([])
    while True:
        jogador = [int(numero) for numero in input().split()]
        if jogador[0] == -1:
            break
        else:
             cartasJogador = Fila()
             for i in jogador:
                 cartasJogador.inserirNoFim(i)
        jogadores[contador].append(cartasJogador)
    contador += 1
for i in range(len(festas)):
    contador = 0
    j = 0
    while True:
        if contador == 1000:
            resultados[i] = 0
            break
        elif j < len(jogadores[i]):
            if isIgual(festas[i], jogadores[i][j]):
                jogadores[i][j].removerDoInicio()
                if jogadores[i][j].isVazia():
                    resultados[i] = j + 1
                    break
                j += 1
            else:
                jogadores[i][j].mandaProFim()
                j += 1
        else:
            j = 0
            festas[i].mandaProFim()
            contador += 1
for i in resultados:
    print(i)