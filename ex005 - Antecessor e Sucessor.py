x = 5+3*11
print(x)

n1 = int(input("Insira um número: "))
n2 = int(input('Insira outro número: '))
s = n1 + n2
ss = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('O valor da soma será {}, o produto será {} e a divisão será {} '.format(s,m,d), end=". ")
print('O valor da divisão inteira {}, e a potência será de {}'.format(di,e))


## Ex 005

num1 = int(input('Digite um número aqui: '))
num2 = num1 - 1
num3 = num1 + 1
print('Seu número é \033[1;31m{}\033[m, que vem depois de \033[1;32m{}\033[m, e antes de \033[1;37m{}\033[m'.format(num1,num2,num3))