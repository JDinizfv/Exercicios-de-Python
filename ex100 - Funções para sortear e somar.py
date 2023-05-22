from random import randint


def sorteio(lista,qtnumeros):
    for i in range(0,qtnumeros):
        lista.append(randint(0,100))
    lista.sort()
    print(f'Sorteando {qtnumeros} valores da lista: ',end='')
    for i in lista:
        print(f'{i}',end=' ')
    print('Pronto!')

def somaPar(num):
    soma=0
    for i in num:
        if i%2==0:
            soma += i
    print(f'Somando os valores pares de: {num}, temos {soma}')

numeros = list()
sorteio(numeros,5)
somaPar(numeros)