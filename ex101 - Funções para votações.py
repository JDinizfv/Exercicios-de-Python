import datetime

def voto(ano=datetime.date.today().year):
    """"
    -> função desenhada para retornar a obrigatoriedade de voto do cidadão, baseado em sua idade.
    :param ano: Ano de Nascimento do Indivíduo.
    :return: sem retorno.
    Função criada por Jean Diniz baseado no exercício 101 do Curso em Video(Python).
    """
    hoje = datetime.date.today().year
    idade = hoje-ano
    print(f'Com {idade} anos: ',end='')
    if 16 <= idade <18 or idade>65:
        print('VOTO OPCIONAL!')
    elif idade<18:
        print('NÃO VOTA!')
    else:
        print('VOTO OBRIGATÓRIO!')


print('-'*25)
ano = int(input('Em que ano você nasceu? '))
voto(ano)