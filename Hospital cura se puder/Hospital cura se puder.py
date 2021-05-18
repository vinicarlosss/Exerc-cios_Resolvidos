def compara_planos(pacientes_e_planos):
    premium, diamante, ouro, prata, bronze, resto = [], [], [], [], [], []
    prioridade = 2
    plano = 1
    for paciente in pacientes_e_planos:
        if paciente[plano] == 'premium':
            premium.append(paciente)
        elif paciente[plano] == 'diamante':
            diamante.append(paciente)
        elif paciente[plano] == 'ouro':
            ouro.append(paciente)
        elif paciente[plano] == 'prata':
            prata.append(paciente)
        elif paciente[plano] == 'bronze':
            bronze.append(paciente)
        else:
            resto.append(paciente)

    premium = sort_reverse(premium) if len(premium) > 1 else premium
    diamante = sort_reverse(diamante) if len(diamante) > 1 else diamante
    ouro = sort_reverse(ouro) if len(ouro) > 1 else ouro
    prata = sort_reverse(prata) if len(prata) > 1 else prata
    bronze = sort_reverse(bronze) if len(bronze) > 1 else bronze
    resto = sort_reverse(resto) if len(resto) > 1 else resto

    return premium+diamante+ouro+prata+bronze+resto


def sort_reverse(lista_de_pacientes):
    prioridade, i = 2, 0
    lista_de_pacientes = list(lista_de_pacientes)
    for paciente in lista_de_pacientes:
        elemento_atual = paciente[prioridade]

        while i > 0 and int(lista_de_pacientes[i-1][prioridade]) < int(elemento_atual):
            lista_de_pacientes[i] = lista_de_pacientes[i - 1]
            i -= 1

        if int(lista_de_pacientes[i][prioridade]) != int(elemento_atual):
            lista_de_pacientes[i] = paciente
        i += 1
    lista_final = ordem_alfabetica(lista_de_pacientes)
    return lista_final

def ordem_alfabetica(lista):
    aux = 0
    prioridade, i, nome = 2, 0, 0
    lista_de_pacientes = list(lista)
    for paciente in lista_de_pacientes:
        elemento_atual = paciente[prioridade]

        while i > 0 and int(lista_de_pacientes[i - 1][prioridade]) == int(elemento_atual):
            if lista_de_pacientes[i-1][nome] > lista_de_pacientes[i][nome]:
                aux = lista_de_pacientes[i]
                lista_de_pacientes[i] = lista_de_pacientes[i - 1]
                lista_de_pacientes[i - 1] = aux
            i -= 1

        if int(lista_de_pacientes[i][prioridade]) != int(elemento_atual):
            lista_de_pacientes[i] = paciente
        i += 1
    return lista_de_pacientes


def saida(lista_final):
    nome = 0
    for paciente in lista_final:
        print(paciente[nome])


n = int(input())
pacientes_e_planos = []
for i in range(n):
    paciente = tuple(map(str, input().split(" ")))
    pacientes_e_planos.append(paciente)

saida(compara_planos(pacientes_e_planos))