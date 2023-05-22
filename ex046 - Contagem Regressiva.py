from time import sleep

num = int(input("Digite um número para a contagem regressiva: "))


for i in range(num,0,-1):
    if i == 1:
        print('{} segundo'.format(i))
    else:
        print('{} segundos'.format(i))

    sleep(1)
print('Fim!')