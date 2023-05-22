num=0

while num>=0:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num<0:
        print('Encerrando programa!')
        break
    print('-' * 20)
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
    print('-' * 20)
print('Fim!')

