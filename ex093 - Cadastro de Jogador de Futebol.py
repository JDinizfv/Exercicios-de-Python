

dados= dict()
dados['Nome do Jogador']= str(input('Nome do Jogador: '))
qtpartidas = int(input(f'Quantas partidas {dados["Nome do Jogador"]} jogou? '))
qtgols = list()
for i in range(1,qtpartidas+1):
    gol = int(input(f'Quantos gols na partida {i}? '))
    qtgols.append(gol)

dados['Gols']=qtgols[:]
dados['Total']= sum(qtgols)
print('-=-'*50)
print(dados)
print('-=-'*50)

for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*50)
print(f'O jogador {dados["Nome do Jogador"]} jogou {len(dados["Gols"])} partidas.')
for i,v in enumerate(qtgols):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
