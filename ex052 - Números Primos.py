num = int(input('Digite um número: '))
j = 0
for i in range(1,num+1):
    if num % i == 0:
        j = j+1
        print('{} é divisivel por {}'.format(num,i))
if j > 2:
    print('Este não é um número primo!')
else:
    print('Este é um número primo!')

## ou

for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(c),end='')