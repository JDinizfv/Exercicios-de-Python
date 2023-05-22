cont = r = num = total = maior = menor = 0

while not r == 'N':
    num = int(input('Digite um número: '))
    total += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = total/cont
print('Você digitou {} números e a média foi {}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))

