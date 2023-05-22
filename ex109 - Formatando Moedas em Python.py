from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,format=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,format=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,format=True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p,13,format=True)}')