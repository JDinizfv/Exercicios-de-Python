a = int(input('Insira o comprimento da reta 1: '))
b = int(input('Insira o comprimento da reta 2: '))
c = int(input('Insira o comprimento da reta 3: '))

if (b-c)<a<(b+c) or (a-c)<b<(a+c) or (a-b)<c<(a+b) is True:
    print('Os valores são válidos para criar um triangulo!')
else:
    print('Valores não são válidos para criação de um triangulo!')
