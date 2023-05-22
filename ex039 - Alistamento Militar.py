
from datetime import date

sexo = int(input('''Qual seu sexo? 
1 - Homem
0 - Mulher 
insira seu sexo: '''))

if sexo == 1:
    nasc = int(input('Qual o ano de nascimento: '))
    ano = date.today().year
    hoje = ano-nasc

    print('Quem nasceu em {}, tem {} anos em {}'.format(nasc,hoje,ano))
    if hoje == 18:
        print('Chegou a hora de se alistar!, Busque imediatamente um posto militar!')
        print('Seu alistamento será este ano!')
    elif hoje > 18:
        print('Já passou da hora de se alistar!, Você deveria ter se alistado a {} anos'.format(hoje-18))
        print('O ano do seu alistamento foi em {}'.format(ano-(hoje-18)))
    elif hoje < 18:
        print('Ainda não é o momento de se alistar! Somente daqui a {} anos'.format(18-hoje))
        print('O ano do seu alistamento será em {}'.format(ano+(18-hoje)))
    else:
        print('Insira um valor válido!')
elif sexo == 0:
    print('Não há necessidade de alistamento obrigatório para mulheres!')