from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    data = int(input('N{}º, digite o seu ano de nascimento: '.format(i)))
    if anoatual - data >= 18:
        maior = maior + 1
        print('Você é maior de idade!')
    elif anoatual - data < 18:
        menor = menor + 1
        print('Você é de menor!')
    else:
        pass

print('''Existem {} pessoas maiores de idade e
{} pessoas menores de idade.'''.format(maior,menor))
