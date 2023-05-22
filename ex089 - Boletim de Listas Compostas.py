lista = list()
aluno = list()
notas = list()

while True:
    aluno.append(str(input('Nome: ')).strip())
    notas.append((int(input('Nota 1: '))))
    notas.append((int(input('Nota 2: '))))
    aluno.append(notas[:])
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        print('Resposta Inválida! Tente Novamente.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*30)
print('Nº Nome',' '*8,'Média')
print('-'*30)
for j,i in enumerate(lista):
    print(f'{lista.index(i)}',end=' ')
    print(f'{lista[lista.index(i)][0]:15}',end=' ')
    print(f'{(lista[j][1][0]+lista[j][1][1])/2}')
print('-'*30)

while True:
    resp2 = int(input('Mostrar qual notas de qual aluno? (999 Interrompe): '))
    if resp2 == 999:
        break
    print(f'Notas de {lista[resp2][0]} são: {lista[resp2][1]}')
    print('-'*30)


