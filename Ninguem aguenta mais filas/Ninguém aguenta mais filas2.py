class No:
    def __init__(self, dado=None):
        self._dado = dado
        self._ant = None
        self._prox = None

    def __str__(self):
        return '{}'.format(self._dado)


class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def isVazia(self):
        if self._inicio == None:
            return True
        return False

    def inserirNoFim(self,dado=None):
        novono = No(dado)
        if self.isVazia():
            self._inicio = self._fim = novono
        else:
            novono._ant = self._fim
            self._fim._prox = novono
            self._fim = novono

    def buscar(self, x):
        i = self._inicio
        while i !=None:
            if x == i._dado:
                break
            else:
                i = i._prox
        return i

    def remover(self, x):
        no_encontrado = self.buscar(x)
        if no_encontrado != None:
            if no_encontrado._ant != None:
                no_encontrado._ant._prox = no_encontrado._prox
            else:
                self._inicio = no_encontrado._prox
            if no_encontrado._prox != None:
                no_encontrado._prox._ant = no_encontrado._ant
            else:
                self._fim = no_encontrado._ant
        return no_encontrado

    def __str__(self):
        s = ''
        i = self._inicio
        while i != None:
            s += '{} '.format(str(i))
            i = i._prox
        return s


n = int(input())
pessoas = [int(numero) for numero in input().split()]
minhafila = Fila()
for i in pessoas:
    minhafila.inserirNoFim(i)
m = int(input())
desistentes = [int(numero) for numero in input().split()]
for i in desistentes:
    minhafila.remover(i)
print(minhafila)