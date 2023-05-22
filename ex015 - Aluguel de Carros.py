dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos Km rodados durante o período?: '))
valorcarro = 60
valorkm = 0.15

print('O valor final será de R${}'.format((dias*valorcarro+km*valorkm)))