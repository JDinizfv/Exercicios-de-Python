texto = str(input('Digite uma frase: ')).upper().strip()

print('Quantas vezes aparece a string ''a ''{}'.format(texto.count('A')))
print('O primeiro : {}'.format(texto.find('A')+1))
print('O último: {}'.format(texto.rfind('A')+1))
