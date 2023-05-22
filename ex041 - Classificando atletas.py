from datetime import date

ano = int(input('Insira o ano de nascimento: '))

date = date.today().year

idade = date - ano

print('Você tem {} anos!'.format(idade))
if idade<= 9:
    print('Você pertence a categoria: MIRIM')
elif idade>9 and idade<=14:
    print('Você pertence a categoria: INFANTIL')
elif idade>14 and idade<=19:
    print('Você pertence a categoria: JUNIOR')
elif idade == 20:
    print('Você pertence a categoria: SÊNIOR')
elif idade>20:
    print('Você pertence a categoria: MASTER')
else:
    print('Insira um valor válido!')