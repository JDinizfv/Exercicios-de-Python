
def ficha(jogador ='<desconhecido>', gols=0):
    """
    -> Cria uma ficha de jogador de futebol.
    :param jogador: Nome do Jogador.
    :param gols: Número de gols na temporada.
    :return: Resumo do dados

    Função criada por Jean Diniz baseado no exercício 103 do Curso em Video(Python).
    """
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')





print('-'*25)
nomejogador = input('Nome do Jogador: ')
numerogols = input('Número de gols: ')

if numerogols.isnumeric() == True:
    numerogols = int(numerogols)
else:
    numerogols=0

if nomejogador.strip() == '':
    ficha(gols=numerogols)
else:
    ficha(nomejogador,numerogols)
