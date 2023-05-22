salario = float(input('Qual o valor do salário analisado?: '))
aumento = 15/100
new = salario+(salario*aumento)

print('Com o reajuste de 15% do valor, seu novo salário será de: R${:.2f}'.format(new))