lista = list()
dados = list()
maior = menor = 0
resp = ''
cont = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if cont == 0:
        menor = dados[1]
        maior = dados[1]
    else:
        if dados[1]>maior:
            maior = dados[1]
        elif dados[1]<menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont +=1
    while resp not in 'SN':
        print('Valor inválido. Tente Novamente!')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)

print(f'Os dados foram {lista}')
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for i in lista:
    if i[1] == maior:
        print(f'[{i[0]}]... ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')
for i in lista:
    if i[1] == menor:
        print(f'[{i[0]}]... ', end='')