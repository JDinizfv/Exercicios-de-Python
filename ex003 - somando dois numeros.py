num1 = int(input('Insira o primeiro número: '))
print(type(num1))
num2 = int(input('Insira o segundo número: '))
print(type(num2))
num3 = num1+num2
num4 = num1-num2
print('A soma dos dois números é: ',num3)

print('A diferença entre \033[33m{}\033[m e \033[35m{}\033[m é igual a \033[36m{}\033[m'.format(num1,num2,num4))

n = input('digite: ')
print(n.isnumeric())
print(n.isalpha())

