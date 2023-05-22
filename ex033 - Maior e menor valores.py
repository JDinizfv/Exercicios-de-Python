


n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

menor = n1

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor valor é {}'.format(menor))

maior = n1

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior valor é {}'.format(maior))


'''if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
else:
    if n2 > n1 and n3 > n1:
        print('{} é o menor número'.format(n1))
    else:
        print('O maior valor é: por números iguais {}'.format(n1))


if n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
else:
    if n3 > n2 and n1 > n2:
        print('{} é o menor número'.format(n2))
    else:
        print('O maior valor é: por números iguais {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('{} é o maior número'.format(n3))
else:
    if n1 > n3 and n2 > n3:
        print('{} é o menor número'.format(n3))
    else:
        print('O maior valor é: por números iguais {}'.format(n3))'''