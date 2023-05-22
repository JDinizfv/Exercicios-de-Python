import random
import time

jogada = int(input(''''Escolha a sua jogada:       
               1.Pedra       
               2.Papel       
               3.Tesoura:     '''))
if jogada == 1:
    print('Você escolheu Pedra')
elif jogada == 2:
    print('Você escolheu Papel!')
elif jogada == 3:
    print('Você escolheu Tesoura!')
else:
    print('Insira um valor válido!')

print('Loading.......')
time.sleep(4)

rol = [1, 2, 3]
cpu = random.choice(rol)

if cpu==1:
    print('CPU escolheu Pedra!!')
elif cpu==2:
    print('CPU escolheu Papel!!')
elif cpu==3:
    print('CPU escolheu Tesoura!!')




print('Então temos que:           ')

time.sleep(2)

if cpu == jogada:
    print('O jogo deu empate!')
elif jogada==1 and cpu ==2:
    print('Você venceu, pedra destroi tesoura!')
elif jogada==1 and cpu == 3:
    print('Você perdeu!! papel envolve pedra!')
elif jogada==2 and cpu== 1:
    print('Você venceu!! papel envolve pedra')
elif jogada==2 and cpu==3:
    print('Você perdeu!! tesoura corta papel')
elif jogada==3 and cpu==1:
    print('Você perdeu!! Pedra destroi Tesoura ')