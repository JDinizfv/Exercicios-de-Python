inicial = int(input('Qual o valor inicial?: '))
razao = int(input('Qual o valor da razão?: '))

c= 1
r = range(inicial, 10, razao)

print('{}'.format(inicial),end=' -> ')
while c<10:
    c += 1
    pa = inicial + (c - 1) * razao
    print('{}'.format(pa),end=' -> ')
print('Fim!')

## OU

primeiro = int(input('Qual o valor inicial?: '))
razão = int(input('Qual o valor da razão?: '))

termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim!')


