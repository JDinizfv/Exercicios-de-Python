dol = 1
cot = 3.28
real = dol * cot

carteira = float(input('Insira o valor atual da sua carteira: '))
valor = carteira / real
print('Sua carteira pode comprar US${:.2f} dólares'.format(valor))