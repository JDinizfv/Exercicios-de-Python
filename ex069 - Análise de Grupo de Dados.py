acima18 = 0
numM = 0
mulheres = 0

while True:
    print('-'*40)
    print(' '*10,'CADASTRE UMA PESSOA',' '*10)
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade>18:
        acima18 += 1
    if sexo == 'M':
        numM += 1
    if sexo == 'F' and idade<20:
        mulheres += 1


    print('-'*20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
    else:
        pass
print(f'Total de pessoas com mais de 18 anos: {acima18}')
print(f'Ao menos temos {numM} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

