from time import sleep
from random import randint

lista = list()
palpite = list()

print('-'*20)
print(f"{'JOGA NA MEGASENA':5}")
print('-'*20)

qt = int(input('Quantos jogos você quer que eu sorteie? '))
print('')
print('-='*5,end='')
print(f' Sorteando {qt:1} Jogos ',end='')
print('-='*5,end='')
print('')

for i in range(0,qt):
    sleep(1)
    print(F'JOGO {i+1}: ',end='')
    for j in range(0,6):
        palpite.append(randint(0,60))
        palpite.sort()
    print(palpite)
    palpite.clear()


print('-='*20)
print('BOA SORTE!!')