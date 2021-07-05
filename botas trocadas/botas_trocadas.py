botas = []
contador = 0
while True:
    try:
        n = int(input())
        if n % 2 != 0 or n > 10**4 or n < 2:
            break
        for i in range(n):
            bota = input()
            botas.append(bota)
            numero = int(bota.split()[0])
            lado = bota.split()[1]
            if numero < 30 or numero >60:
                break
            elif lado != "D" and lado != "E":
                break
            elif lado == 'D':
                if '{} {}'.format(numero, 'E') in botas:
                    contador+=1
                    botas.remove('{} {}'.format(numero, 'E'))
                    botas.remove('{} {}'.format(numero, 'D'))
                if i == n - 1:
                    print(contador)
            elif lado == 'E':
                if '{} {}'.format(numero, 'D') in botas:
                    contador += 1
                    botas.remove('{} {}'.format(numero, 'E'))
                    botas.remove('{} {}'.format(numero, 'D'))
                if i == n - 1:
                    print(contador)
        break
    except:
        break