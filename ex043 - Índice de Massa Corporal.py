peso = float(input('Qual seu peso(kg)?: '))
altura = float(input('Qual sua altura(m)'))

imc = peso / (altura**2)

print('Seu IMC é de {} pontos'.format(imc))

if imc <18.5:
    print('Seu imc foi de {}, você está abaixo do peso!'.format(imc))
elif 18.5 <= imc <25:
    print('Seu imc foi de {}, você está no peso ideal!'.format(imc))
elif 25 <= imc< 30:
    print('Seu imc foi de {}, você está no sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc foi de {}, você está obeso!'.format(imc))
elif imc>=40:
    print('Seu imc foi de {}, você está em obesidade mórbida!'.format(imc))
