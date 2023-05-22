from time import sleep

def contador(inicio,fim,passo):
    print('-='*20)
    if passo<0:
        passo = -(passo)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    elif passo>0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    elif passo == 0:
        passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    if inicio<fim:
        cont = inicio
        while cont<= fim:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont+= passo
        print('Fim!')
    else:
        cont = inicio
        while cont>=fim:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont -=passo
        print('Fim!')
sleep(1)
contador(1,10,1)
sleep(1)
contador(10,0,2)
sleep(1)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
sleep(1)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)