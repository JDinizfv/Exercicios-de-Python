inicial = int(input('Qual o valor inicial?: '))
razao = int(input('Qual o valor da razão?: '))

pas = 0
for i in range(1,11):
    pa = inicial + (i-1)*razao
    print('{} '.format(pa),end='-> ')
print('Fim!')

decimo = inicial + (10-1)*razao
for c in range(inicial, decimo + razao, razao):
    print('{}'.format(c),end=' -> ')
print('Acabou!')

