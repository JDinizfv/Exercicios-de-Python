
tupla = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar',
         'mercado','programador','futuro')
vogais = ('a','e','i','o','u')

for i in tupla:
    print(f'\nNa palavra {str(i).upper().strip()} temos ',end='')
    for j in i:
        if j in vogais:
            print(f'{j}',end=' ')

