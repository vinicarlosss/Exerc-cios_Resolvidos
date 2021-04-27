def juvenal(n):
    global c1
    c1 += 1
    if n == 1:

        return 1

    elif n % 2 == 0:

        return juvenal(n/2)
    else:

        return juvenal(3*n+1)


def g():
    global c_total
    global aux
    if c_total > aux:
        aux = c_total

n = 0
t = int(input())
casos = []
while t > 0:
    t -= 1
    (a,b) =[int(numero) for numero in input().split()]
    casos.append(a)
    casos.append(b)
while len(casos) > 0:
    n+= 1
    a = casos[0]
    b = casos[1]
    c_total = 0
    aux = 0

    for e in range(a,b+1):

        c1 = 0
        juvenal(e)
        c_total = c1
        g()

    print(f"Caso {n}:",aux)

    del casos[0]
    del casos[0]








