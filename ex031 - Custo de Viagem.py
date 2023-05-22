viagem = int(input('Qual a distância(km) do seu destino? '))
if viagem <= 200:
    fee = 0.50
    preco = viagem * fee
    print('Viagem de {} km, terá um custo de R${} por km. Portanto, o valor total da sua viagem será de R${}'.format(viagem,fee,preco))
else:
    fee = 0.45
    preco = viagem* fee
    print('Viagem de {} km, terá um custo de R${} por km. Portanto, o valor total da sua viagem será de R${}'.format(viagem,fee,preco))