texto = str(input('Digite o seu nome completo: ')).strip()

#O nome com todas as letras maiúsculas
print('O nome com todas as letras maiúsculas é: ',texto.upper())

# O nome com todas as minúsculas
print('O nome com todas minúsculas é: ',texto.lower())

#Quantas letras ao todo?
print('O número de letras do seu nome é de: ',len(texto) - texto.count(' '))



#Quantas letras tem o primeiro nome?
texto_sep = texto.split()
print('O primeiro nome é: ',texto_sep[0])
print('O número de caracteres é de: ',len(texto_sep[0]))
