salario = int(input('Qual o valor do seu salário?: '))

if salario<=1250:
   aumento = salario * 1.15
else:
    aumento = salario* 1.10
print('Hoje seu salário é R${:.2f}. Seu novo salário será de: \033[4;31mR${:.2f}\033[m'.format(salario,aumento))