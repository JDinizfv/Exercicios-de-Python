print('¨Preciso de 6 números!!!')

j = 0
for i in range(1,7):
    num = int(input('Digite o {}º número: '.format(i)))
    if num % 2 == 0:
        j = j + num
        print(j)
    else: pass

print('Total: {}'.format(j))

print('Fim!')