print('-'*20,'BANCO DO BRASIL','-'*20)
print('-'*60)
print(' ')
print('='*60)
print('Bem vindo ao caixa eletrônico do BB.')
resgate = int(input('Digite o valor que deseja sacar: '))
montante = resgate

cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0

while True:
    if montante % 50 != 0:
        pass
    cont50 = int(montante/50)
    montante = int(montante - (cont50*50))
    if montante == 0:
        break
    if montante % 20 != 0:
        pass
    cont20 = int(montante/20)
    montante = int(montante - (cont20*20))
    if montante ==0:
        break
    if montante % 10 != 0:
        pass
    cont10 = int(montante/10)
    montante = int(montante - (cont10*10))
    if montante ==0:
        break
    if montante % 5 != 0:
        pass
    cont5 = int(montante/5)
    montante =int(montante - cont5*5)
    if montante == 0:
        break
    if montante % 2 != 0:
        pass
    cont2 = int(montante/2)
    montante = int(montante-cont2*2)
    if montante == 0:
        break
    cont1 = int(montante/1)
    montante = int(montante-cont1*1)
    break


if cont50 != 0:
    print(f'Total de {cont50} células de R$50')
if cont20 != 0:
    print(f'Total de {cont20} células de R$20')
if cont10 != 0:
    print(f'Total de {cont10} células de R$10')
if cont5 != 0:
    print(f'Total de {cont5} células de R$5')
if cont2 != 0:
    print(f'Total de {cont2} células de R$2')
if cont1 != 0:
    print(f'Total de {cont1} células de R$1')

print('='*60)

print('Volte sempre ao Banco do Brasil! Tenha um bom dia!')




