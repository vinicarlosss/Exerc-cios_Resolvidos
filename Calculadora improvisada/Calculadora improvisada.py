def Suc(termo1):
    return termo1 + 1

def Soma(termo1,termo2):

    for e in range(termo2):
        termo1 += 1
    return termo1

def Mult(termo1,termo2):

    contador = 0
    mult = 0
    for e in range (termo2):
        while (contador < termo1):

            contador += 1
            mult += 1
        contador = 0
    return mult

def Exp(termo1,termo2):

    c = 1
    for e in range(termo2):
        c = Mult(c, termo1)
    return c






while True:

    linha_de_entrada = input().split()

    operador = linha_de_entrada[0]
    try:
        termo1, termo2 =int(linha_de_entrada[1]), int(linha_de_entrada[2])


    except:
        termo1 = int(linha_de_entrada[1])


    if operador == "Suc":
        print(Suc(termo1))

    elif operador == "Soma":
        print(Soma(termo1,termo2))

    elif operador == "Multi":
        print(Mult(termo1,termo2))
    elif operador == "Exp":
        print(Exp(termo1,termo2))
    else:
        break