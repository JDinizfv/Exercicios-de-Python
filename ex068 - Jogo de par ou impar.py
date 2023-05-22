from random import randint

print('Bem vindo ao jogo do Par ou Ímpar')
print('-=-'*20)



jogador = 0
cpu = 0

while not cpu == 1:
    cpunum = randint(0,10)
    num = int(input('Diga um valor: '))
    escolha = 'T'
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().split()[0]
    resultado = cpunum + num

    print('-'*20)
    print(f'Você jogou {num} e o computador {cpunum}. Total de {resultado}')
    print('-'*20)
    if escolha == 'P' and resultado % 2 == 0:
        jogador += 1
        print('Você VENCEU!')
    elif escolha == 'I' and resultado % 2 != 0:
        jogador += 1
        print('Você VENCEU!')
    elif escolha == 'P' and resultado % 2 != 0:
        cpu += 1
        print('Você PERDEU!')
    elif escolha == 'I' and resultado % 2 == 0:
        cpu+=1
        print('Você PERDEU!')
print('-=-'*20)
print(f'GAME OVER! Você venceu {jogador} vezes.')
print('Obrigado por jogar!')

vitorias = 0
'''while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = str(0)
    while tipo not in 'PI':
        tipo = str(input('Escolha Par ou Ímpar? [P/I] ')).upper().split()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
print('-=-'*20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
print('Obrigado por jogar!')
'''
