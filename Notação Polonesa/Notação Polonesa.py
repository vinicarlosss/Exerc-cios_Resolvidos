class No:
    def __init__(self, dado=None):
        self._dado = dado
        self._prox = None


class Pilha:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def isVazia(self):
        if self._inicio == None:
            return True
        return False

    def inserirNoComeço(self, dado):
        novono = No(dado)
        if self.isVazia():
            self._fim = novono
        else:
            novono._prox = self._inicio
        self._inicio = novono

    def removerDoInicio(self):
        no = self._inicio
        if not self.isVazia():
            if no._prox == None:
                self._fim = None
            self._inicio = no._prox
        return no._dado


def operacao(termoA, termoB, operador):
    if operador == '+':
        return termoA + termoB
    elif operador == '-':
        return termoA - termoB
    elif operador == '*':
        return termoA * termoB
    elif operador == '/':
        if termoA / termoB > 0:
            return termoA // termoB
        return int(-(-(termoA/termoB)//1))


while True:
    try:
        expressao = input().split()
        expressao.reverse()
        operando = Pilha()
        for i in expressao:
            if not i == '+' and not i == '-' and not i == '*' and not i == '/':
                i = int(i)
                operando.inserirNoComeço(i)
            else:
                operando1 = operando.removerDoInicio()
                operando2 = operando.removerDoInicio()
                operando.inserirNoComeço(operacao(operando1, operando2, i))
        print(operando.removerDoInicio())
    except:
        break