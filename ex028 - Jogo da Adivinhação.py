import random
from time import sleep

print('Bem vindo ao game da adivinhação')
rol = [1,2,3,4,5]
sorteio = random.choice(rol)
escolha = int(input('Escolha um número de 1 a 5: '))

print('PROCESSANDO......')
sleep(3)
if escolha>5 or escolha<1:
    print('Insira um valor válido!')
else:
    if sorteio == escolha:
        print('Parabéns você acertou !! O número escolhido foi {}'.format(sorteio))
    else:
        print('Não foi dessa vez, o número escolhido pela maquina foi {}'.format(sorteio))
print('Fim de Jogo!')
