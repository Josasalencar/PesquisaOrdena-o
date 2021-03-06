import itertools as it
import timeit

def CountingSort(array):
    maxValue = max(array) + 1
    count = [0] * maxValue
    
    for i in array:
        count[i] += 1
    i = 0
    for j in range(maxValue):
        for k in range(count[j]):
            array[i] = j
            i += 1
    return array

def RadixSort(array):
    m = max(array)
    
    i = 1
    while(m/i > 0):
        CountingSort(array)
        
        i*=10

lista = list(it.permutations([1, 2, 3, 4, 5, 6], 6))
listaAux = []
listaPermut = []

for i in lista:
    listaAux.append(list(i))
    listaPermut.append(list(i))

tempos = []


for i in listaPermut:
    tempos.append(timeit.timeit('bucketSort({})'.format(i),setup="from __main__ import bucketSort",number=50))

maxIdx = tempos.index(max(tempos))
minIdx = tempos.index(min(tempos))

print('Pior caso: ', listaAux[maxIdx])
print('Melhor caso: ', listaAux[minIdx])
