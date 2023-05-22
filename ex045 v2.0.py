from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Qual é a sua jogada?: 
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual é a sua jogada?: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(2)

print('-='*11)
print('CPU jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0 :
    if jogador == 0:
        print('Jogo deu Empate!')
    elif jogador == 1:
        print('Jogador Venceu! Papel engole Pedra')
    elif jogador == 2:
        print('Computador Venceu! Pedra amassa Tesoura!')
    else:
        print('Jogada INVÁLIDA!')

elif computador == 1 :
    if jogador == 0:
        print('Computador Venceu! papel envolve pedra')
    elif jogador == 1:
        print('Jogo deu Empate!')
    elif jogador == 2:
         print('Jogador Venceu! tesoura corta papel')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2 :
    if jogador == 0:
        print('Jogador Venceu! Pedra amassa tesoura')
    elif jogador == 1:
        print('Computador Venceu! Tesoura corta papel')
    elif jogador == 2:
        print('Jogo deu Empate!')
    else:
        print('Jogada INVÁLIDA!')
