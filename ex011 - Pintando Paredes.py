altura = float(input('Digite a altura da parede: '))
largura = float(input("Digite a largura da parede: "))

parede = altura * largura
lata_tinta = 2
res = int(parede / lata_tinta)

print('O valor necessário de latas de tinta para pintar toda parede ({} metros), será de {} latas de 1L.'.format(parede,res))