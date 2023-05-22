
brasileiro = ('Botafogo','Palmeiras','Cruzeiro','Fortaleza','São Paulo','Fluminense','Grêmio',
              'Internacional','Bahia','Athletico Paranaense','Vasco da Gama','Red Bull Bragantino','Cuiába',
              'Santos','Atlético MG','Flamengo','Corinthians','Goiás','Coritiba','América MG')
print('-=-'*15)
print(f'Lista de Times do Brasileirão 2023: {brasileiro}')
print('-=-'*15)
print(f'Os 5 primeiros são: {brasileiro[0:5]}')
print('-=-'*15)
print(f'Os 4 últimos são: {brasileiro[-4:]}')
print('-=-'*15)
print(f'Times em ordem alfabética {sorted(brasileiro)}')
print('-=-'*15)
print(f"O Fortaleza está na {brasileiro.index('Fortaleza')+1}º posição!")
print('-=-'*15)
escolha = int(input('Escolha qual colocado deseja observar: '))
for pos,brasileiro in enumerate(brasileiro):
    if escolha == pos+1:
        print(f'O {brasileiro} está na {pos+1}º posição')
print('-=-'*15)