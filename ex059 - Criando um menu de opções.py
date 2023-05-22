from time import sleep

print('Bem vindo ao Informador Simplificado!')
sleep(1)
n = -1


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('-'*10,'MENU','-'*10)


while not n == 5:
    print('')

    print('-' * 10, 'MENU', '-' * 10)
    print('''Escolha uma função: 
        [ 1 ] - Somar 
        [ 2 ] - Multiplicar 
        [ 3 ] - Maior 
        [ 4 ] - Novos Números
        [ 5 ] - Sair do Programa''')
    n = int(input('Escolha a função desejada: '))

    if n == 1:
        sleep(1)
        print('A soma de {} e {} é igual a {}'.format(n1,n2,n1+n2))
    elif n == 2:
        sleep(1)
        print('A multiplicação de {} e {} é igual a {}'.format(n1,n2,n1+n2))
    elif n == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        elif n2 == n1:
            maior = n1
            print('Os valores são iguais...Portanto...')
        print('O maior valor é: {}'.format(maior))
    elif n == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif n == 5:
        print('Encerrando!!')
        sleep(1)
    else:
        print('Insira um número válido')


sleep(1)
print('Obrigado por usar o programa!')

