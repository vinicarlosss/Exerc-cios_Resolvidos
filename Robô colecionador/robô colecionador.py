rali = []
while True:
    n, m, s = [int(numero) for numero in input().split()]
    if n == 0 and m == 0 and s == 0:
        break
    robo = None
    posicao_robo = [None for _ in range(2)]
    arena = [[int(e) for e in range(m)] for _ in range(n)]
    for i in range(n):
        celula = input()
        for j in range(m):
            arena[i][j] = celula[j]
        if robo == None:
            c = 0
            for j in celula:
                if j == "N" or j == "S" or j == "L" or j == "O":
                    robo = arena[i][c]
                    posicao_robo[0] = i
                    posicao_robo[1] = c
                c += 1
    instrucao = input()
    figurinhas = 0
    for i in instrucao:
        if i == "F":
            if robo == "N":
                posicao_robo[0] -= 1
                if posicao_robo[0] < 0 or arena[posicao_robo[0]][posicao_robo[1]] == "#":
                    posicao_robo[0] += 1
                elif arena[posicao_robo[0]][posicao_robo[1]] == "*":
                    arena[posicao_robo[0]][posicao_robo[1]] = "."
                    figurinhas += 1
            elif robo == "S":
                posicao_robo[0] += 1
                if posicao_robo[0] == n or arena[posicao_robo[0]][posicao_robo[1]] == "#":
                    posicao_robo[0] -= 1
                elif arena[posicao_robo[0]][posicao_robo[1]] == "*":
                    arena[posicao_robo[0]][posicao_robo[1]] = "."
                    figurinhas += 1
            elif robo == "O":
                posicao_robo[1] -= 1
                if posicao_robo[1] < 0 or arena[posicao_robo[0]][posicao_robo[1]] == "#":
                    posicao_robo[1] += 1
                elif arena[posicao_robo[0]][posicao_robo[1]] == "*":
                    arena[posicao_robo[0]][posicao_robo[1]] = "."
                    figurinhas += 1
            elif robo == "L":
                posicao_robo[1] += 1
                if posicao_robo[1] == m or arena[posicao_robo[0]][posicao_robo[1]] == "#":
                    posicao_robo[1] -= 1
                elif arena[posicao_robo[0]][posicao_robo[1]] == "*":
                    arena[posicao_robo[0]][posicao_robo[1]] = "."
                    figurinhas += 1
        else:
            if robo == "N" and i == "D":
                robo = "L"
            elif robo == "N" and i == "E":
                robo = "O"

            elif robo == "L" and i == "D":
                robo = "S"
            elif robo == "L" and i == "E":
                robo = "N"

            elif robo == "S" and i == "D":
                robo = "O"
            elif robo == "S" and i == "E":
                robo = "L"

            elif robo == "O" and i == "D":
                robo = "N"
            elif robo == "O" and i == "E":
                robo = "S"
    rali.append(figurinhas)
for i in rali:
    print(i)