#entradas

xa0, ya0, xa1, ya1 = [int(ponto) for ponto in input().split()]
xb0, yb0, xb1, yb1 = [int(ponto) for ponto in input().split()]

#algoritimo para verificar colisão"

#condição verifica se o par ordenado mais baixo do retângulo B não colide com o par ordenado mais alto do retangulo A no eixo X"
#ou se o par ordenado mais alto do retângulo B não colide com o par ordenado mais baixo do retângulo A no eixo X "
#Se uma das condições for atendida o programa presume que os retângulos não colidem, caso contrário ele parte para a outra condição"

if xb0 > xa1  or xb1 < xa0:
    print("0")

#condição verifica se o par ordenado mais baixo do retângulo B não colide com o par ordenado mais alto do retangulo A no eixo Y"
#ou se o par ordenado mais alto do retângulo B não colide com o par ordenado mais baixo do retângulo A no eixo Y "
#Se uma das condições for atendida o programa presume que os retângulos não colidem, caso contrário ele parte para a outra condição"

elif yb0 > ya1 or yb1 < ya0:
    print("0")

#Caso nenhuma dentre todas as condições for atendida o programa entende que os triângulos colidem entre si.

else:
    print("1")














