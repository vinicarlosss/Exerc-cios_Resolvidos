pessoa = int(input())       # a variável pessoa define o número de pessoas que usam a escada
sensor = []         #array sensor contém o tempo que cada pessoa passou pelo sensor
contador = 0
tempo = 0


while (contador < pessoa):                   #repetição para serem inseridos os tempos que cada pessoa passou pelo sensor

        sensor.append(int(input()))              #nessa linha o programa adiciona o tempo que cada pessoa passou pelo sensor no array sensor
        contador += 1


contador = 1

while True:                 #repetição para calcular o tempo que a escada se mantém ligada.
    try:

        for e in sensor:               #laço for em cada elemento do array sensor

            modulo = sensor[contador] - e  # a variável modulo calcula a distância entre os módulos de cada elemento do array sensor
            contador += 1           #incrementa 1 no contador fazendo com que na próxima iteração o modulo seja calculado com o próximo elemento do array sensor
            tempo += modulo         #é incrementado a distância entre os módulos de cada elementos da lista na variável tempo para indicar o tempo que a escada está funcionando

    except:       #quando o contador excede o número de indíces do array sensor ele parte para a excessão
        tempo += 10        #incrimenta os primeiros 10 segundos de quando a primeira pessoa passou pelo sensor
        print(tempo)
        break


