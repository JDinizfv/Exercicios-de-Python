from random import randint
from time import sleep
from operator import itemgetter



resultados = dict()
ranking = dict()
print('Valores sorteados: ')
sleep(1)
for i in range(1,5):
    resultados[f'Jogador{i}']= randint(1,6)
    print(f"    O Jogador{i} tirou {resultados[f'Jogador{i}']}")
    sleep(1)
print('-='*30)
print('==Ranking dos jogadores ==')
ranking = sorted(resultados.items(), key=itemgetter(1),reverse=True)
print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
