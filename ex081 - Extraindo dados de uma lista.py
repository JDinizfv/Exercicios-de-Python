
lista = list()

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    print('Valor adicionado com sucesso!')
    resp = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        print('Digite uma resposta válida!')
        resp = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(lista)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')
