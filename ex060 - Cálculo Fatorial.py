from math import factorial

print('Bem vindo ao Calculador Fatorial')
n = int(input('Escolha o número fatorial desejado: '))
f = factorial(n)
print('O fatorial de {}! é igual a: {}'.format(n,f))

## ---------------------- 2 º Forma
fatorial = 1

for i in range(n,0,-1):
    print(i,end=' x ')
    fatorial = fatorial * i
    print(fatorial)
print('Fatorial de {} é: {}'.format(n,fatorial))

print('-=-'*20)
#--------------------------------------------------------- 3º Forma-----
m = int(input('Escolha o número fatorial desejado: '))
c = m

factorial = 1


print('Calculando {}! '.format(m),end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c >1 else ' = ',end='')
    factorial = factorial * c
    c -= 1

print('{}'.format(factorial))