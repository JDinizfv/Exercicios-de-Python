nome = str(input('Digite seu nome: ')).strip()
check = int(nome.find('Silva'))

if check >= 0:
    print('Você é um Silva!!')
else:
    print('Você não é um silva!')

## ou

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))