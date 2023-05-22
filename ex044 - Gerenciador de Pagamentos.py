valor = float(input('Insira o valor do produto: '))
print('O Valor do produto é de R${}'.format(valor))

print('Insira o tipo de pagamento: '
      '1. À vista(dinheiro/cheque) '
      '2. À vista(cartão) '
      '3. 2x no cartão '
      '4. 3x ou mais no cartão ')
pag = int(input('Qual você deseja: '))

if pag == 1:
    valor = valor-(valor*0.10)
    print('Com 10% de desconto, o valor do pagamento será de R${}'.format(valor))
elif pag == 2:
    valor= valor-(valor*0.05)
    print('Com 5% de desconto, o valor do pagamento será de R${}'.format(valor))
elif pag == 3:
    parcela = valor/2
    print('Valor total do pagamento será de R${}, dividido em 2 parcelas de R${}'.format(valor,parcela))
elif pag == 4:
    valor = valor*1.2
    totparc = int(input('Em quantas parcelas deseja comprar?: '))
    parcela = valor/totparc
    print('O valor total do pagamento será de R${}, dividido em {} parcelas de R$ {}'.format(valor,totparc,parcela))
else:
    print('Insira um valor válido!')