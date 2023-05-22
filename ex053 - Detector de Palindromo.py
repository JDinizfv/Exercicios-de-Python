frase = str(input('Digite sua frase: ').upper().strip())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a frase {}'.format(junto))

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um palíndromo')









