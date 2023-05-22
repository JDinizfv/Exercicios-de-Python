import random
from time import sleep

print('Bem vindo ao game da adivinhação v2.0')
sleep(1)
rol = range(0,11)
maquina = random.choice(rol)
jogador = -1
tentativas = 0

print('Vamos começar?...')
sleep(1)
while not jogador == maquina:
    jogador = int(input('Adivinhe qual número escolhido pela máquina (0 a 10): '))
    if jogador != maquina:
        print('Número errado, tente novamente!')
        tentativas += 1
        sleep(1)
print('---'*11)
print('Parabéns você conseguiu adivinhar depois de {} tentativas! O número escolhido pela maquina foi o número {}'.format(tentativas,maquina))
print('Obrigado por jogar!')