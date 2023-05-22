import math
angulo = float(input('Digite o valor do angulo: '))
rad = math.radians(angulo)

print('O valor em radianos do angulo {}, é de {:.2f} radianos. '.format(angulo,rad))
print('O Seno do angulo {}, é {:.2f}.'.format(angulo,math.sin(rad)))
print('O Cosseno do angulo {}, é {:.2f}'.format(angulo,math.cos(rad)))
print('A Tangente do angulo {}, é {:.2f}'.format(angulo,math.tan(rad)))