def quicksort(V):
    if len(V) <= 1:
        return V

    pivot = V[0]
    equal = [x for x in V if x == pivot]
    lesser = [x for x in V if x < pivot]
    greater = [x for x in V if x > pivot]
    return quicksort(lesser) + equal + quicksort(greater)


numero = int(input())
V = [int(numero) for numero in input().split()]
quicksort(V)
for e in range (1,numero+1):
    if e not in V:
        print(e)
        break




