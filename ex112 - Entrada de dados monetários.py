from ex111.utilidadescev import dado
from ex111.utilidadescev import moeda




p = dado.leiadinheiro('Digite o preço: R$')
print(p)
print(type(p))

#d = float(input('Digite o preço: R$'))
#moeda.resumo(d,30,15)

moeda.resumo(p,20,30)

