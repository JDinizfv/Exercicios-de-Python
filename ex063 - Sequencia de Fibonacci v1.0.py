print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
num = int(input('Quantos números você quer mostrar? '))

n = 2
f1 = 0
f2 = 1
f3 = 0

print('-=-'*30)
print('{} -> {}'.format(f1,f2),end=' -> ')
while n != num:
    f3 = f1 + f2
    print(f3,end=' -> ')
    f1 = f2
    f2 = f3
    n += 1
print('Fim!')
print('-=-'*30)

