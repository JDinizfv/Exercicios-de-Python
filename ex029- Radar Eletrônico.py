velocidade = int(input('Digite o valor em km da velocidade do veículo: '))
taxa = 7
multa = (velocidade-80)*taxa

if velocidade>80:
    print('Você foi multado por velocidade excessiva')
    print('Sua multa será de R${}'.format(multa))
else:
    print('Velocidade regular permitida!')