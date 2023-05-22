lista = list()
listapar = []
listaimpar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    resp = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        print('Digite uma resposta válida!')
        resp = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

print(f'A lista completa é: {lista}')
for i in lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)
print(f'A lista de pares é: {listapar}')
print(f'A lista de ímpares é: {listaimpar}')