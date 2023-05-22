sexo = ''

while not sexo != 'M' or sexo != 'F':
    sexo = str(input('Digite o sexo [M|F]: ').strip().upper()[0])

    if sexo == 'M':
        print('Seu sexo é Masculino!')
    elif sexo == 'F':
        print('Seu sexo é Feminino!')
    elif sexo !='M'or sexo != 'F':
        print('Insira um digito válido!')

print('Fim!')


sex = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

while sex not in 'MmFf':
    sex = str(input('Dados Inválidos! Por favor digite o seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sex))
