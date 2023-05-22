print('-'*40)
print(' '*10,'LOJAS SUPER BARATÃO',' '*10)

total = 0
acima1000 = 0
maisbarato = ' '
preçobarato = 0
count = 0

while True:
    nome = str(input('Nome do produto: ')).upper().strip()
    preço = float(input('Preço do produto: R$'))
    count += 1
    total += preço
    if preço>1000:
        acima1000 += 1
    if count == 1:
        maisbarato = nome
        preçobarato = preço
    else:
        if preço<preçobarato:
            preçobarato=preço
            maisbarato = nome

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=-'*40)
print(f'Temos {acima1000} produtos acima de R$1000.')
print(f'O produto mais barato foi {maisbarato}, e custou R${preçobarato:.2f}')
print(f'O total da compra foi de R${total}')
print('Fim!')

