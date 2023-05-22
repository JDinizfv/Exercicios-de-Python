import math
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjascente: '))
h = math.sqrt(math.pow(co,2)+math.pow(ca,2))

print('O valor da hipotenusa será de {}'.format(h))

