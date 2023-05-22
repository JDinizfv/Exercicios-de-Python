matrix = list()
dados = list()
numpar = 0
num3col = 0
maior2linha = list()


for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Digite um valor para [{i},{j}] '))
        if num % 2 ==0:
            numpar += num
        dados.append(num)
        print(dados)
        if j == 2:
            num3col += num
        if i == 1:
            maior2linha.append(num)
    matrix.append(dados[:])
    dados.clear()
print('-='*30)

maior2linha = max(maior2linha)

for i in matrix:
    for j in i:
        print(f'[ {j:1} ]',end=' ')
    print('\n',end='')
print('-='*30)
print(f'A soma dos valores pares é {numpar}' )
print(f'A soma dos valores na 3º coluna é {num3col}')
print(f'O maior valor da 2ª linha é {maior2linha}')