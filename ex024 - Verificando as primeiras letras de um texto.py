nome = str(input('Digite o nome da sua cidade: ')).strip()
nomea = nome.upper()
check2 = nomea.startswith('SANTO')

## ou

print(nomea[:5] == 'SANTO')

print(check2)

