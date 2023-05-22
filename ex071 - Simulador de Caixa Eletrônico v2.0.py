print('='*20,'BANCO DO BRASIL','='*20)
print('='*60)
print(' ')
print('='*60)
print('Bem vindo ao caixa eletrônico do BB.')
resgate = int(input('Digite o valor que deseja sacar: '))
montante = resgate
ced = 50
totced = 0
while True:
    if montante >= ced:
        montante -= ced
        totced += 1
    else:
        if totced >0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced=0
        if montante == 0:
            break
