def remove(lista, id):
    for n in id:
        if n in lista:
            i = lista.index(n)
            lista.pop(i)
    return lista


n = int(input())
fila = list(map(int, input().split(" ")))
m = int(input())
deixaram_fila = list(map(int, input().split(" ")))
fila_final = remove(fila, deixaram_fila)
for id in fila_final:
    print(id, end=" ")
