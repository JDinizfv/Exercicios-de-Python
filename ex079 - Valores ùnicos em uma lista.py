lista = list()
resp = 'n'
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor Adicionado com Sucesso...')
    resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    while not resp in 'SNsn':
        print('Insira uma resposta válida!')
        resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resp in 'Nn':
        print('Encerrando programa...')
        break
print('-='*30)
lista.sort()
print(lista)