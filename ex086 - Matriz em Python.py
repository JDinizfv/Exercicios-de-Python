matrix = list()
dados = list()

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Digite um valor para [{i},{j}] '))
        dados.append(num)
        print(dados)
    matrix.append(dados[:])
    dados.clear()
print('-='*30)

for i in matrix:
    for j in i:
        print(f'[ {j:^5} ]',end=' ')
    print('\n',end='')
