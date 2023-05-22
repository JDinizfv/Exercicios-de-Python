from random import randint
from time import sleep

print('Bem vindo ao game da adivinhação v3.0')
sleep(1)
maquina = randint(0,11)

jogador = -1
tentativas = 0

print('Vamos começar?...')
sleep(1)
print('Tente adivinhar o número escolhido pela máquina')
sleep(1)
print('A máquina acabou de escolher um número...')
while not jogador == maquina:


    print('')
    jogador = int(input('Adivinhe qual número escolhido pela máquina (0 a 10): '))
    if jogador != maquina:
        print('Número incorreto! Tente novamente')
        if jogador > maquina:
            print('Tente um número menor...')
        elif jogador < maquina:
            print('Tente um número maior...')
    tentativas += 1
    sleep(1)
print('---'*11)
print('Parabéns você conseguiu adivinhar depois de {} tentativas! O número escolhido pela maquina foi o número {}'.format(tentativas,maquina))
print('Obrigado por jogar!')