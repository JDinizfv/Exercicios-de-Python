e = int(input('Escolha um número para a tabuada: '))
tab = range(1,11)

print('')
print('SOMA')
for i in tab:
    s = e+i
    print('{} + {} = {}'.format(e,i,s))
print('')
print('SUBTRAÇÃO')
for i in tab:
    sub = e-i
    print('{} - {} = {}'.format(e, i, sub))
print('')
print('MULTIPLICAÇÃO')
for i in tab:
    m = e*i
    print('{} * {} = {}'.format(e, i,m ))
print('')
print('DIVISÃO')
for i in tab:
    div = e/i
    print('{} / {} = {}'.format(e, i, div))


