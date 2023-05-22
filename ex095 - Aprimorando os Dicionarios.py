

lista= list()
dados= dict()
qtgols = list()
totalgols = 0


while True:
    print('-' * 30)
    dados['Nome do Jogador']= str(input('Nome do Jogador: '))
    qtpartidas = int(input(f'Quantas partidas {dados["Nome do Jogador"]} jogou? '))
    qtgols.clear()
    for i in range(1,qtpartidas+1):
        gol = int(input(f'Quantos gols na partida {i}? '))
        qtgols.append(gol)
        totalgols += gol
    dados['Gols']=qtgols[:]
    dados['Total']=totalgols
    lista.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SnNn':
        print('Insira uma resposta válida!')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=-'*50)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total"}')
print('-' * 50)
for i,j in enumerate(lista):
    print(f'{i:<4} ',end='')
    for d in j.values():
        print(f'{str(d):<15} ',end= '')
    print()
while True:
    print('-' * 30)
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar) '))
    if busca == 999:
        break
    if busca>=len(lista):
        print(f'ERRO! não existe jogador com o código {busca}! Tente Novamente. ')
    else:
        print(F'-- LEVANTAMENTO JOGADOR {lista[busca]["Nome do Jogador"]}:')

        for i,g in enumerate(lista[busca]['Gols']):
                print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<<VOLTE SEMPRE>>>')

