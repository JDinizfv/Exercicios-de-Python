import time
valor = float(input('Qual o valor da Casa?: '))
salario = float(input('Qual o valor do salário?: '))
anos = int(input('Em quantos anos deseja pagar?: '))

pmt = valor/(anos*12)
print(pmt)
print('Analisando....')
time.sleep(3)
if pmt>(salario*0.30):
    print('Seu empréstimo não será aprovado!!')
else:
    print('Seu empréstimo foi aprovado!! Com parcelas de R${:.2f} mensais'.format(pmt))