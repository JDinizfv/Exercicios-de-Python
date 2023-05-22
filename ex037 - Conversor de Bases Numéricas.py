num = int(input('Insira um número inteiro qualquer: '))
print('''Agora escolha qual será a base de conversão
      - 1. Binário
      - 2. Octal
      - 3. Hexadecimal''')
escolha = int(input('Qual opção deseja escolher (1,2 ou 3)?: '))

if escolha == 1:
      print('{} convertido para binário, é igual a {}'.format(num,bin(num)[2:]))
elif escolha == 2:
      print('{} convertido para octal, é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
      print('{} convertido para hexadecimal, é igual a {}'.format(num, hex(num)[2:]))
else:
      print('Escolha um valor válido!')

