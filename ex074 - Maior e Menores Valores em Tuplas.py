from random import randint
from random import randrange

rol = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os valores sorteados foram: {rol}')

maior = menor = 0
for i in rol:
    menor=i
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')

# Versão Professor
print('OS VALORES SORTEADOS FORAM OS: ',end='')
for n in rol:
    print(f'{n} ', end='')
print(f'\nO MAIOR VALOR FOI: {max(rol)}')
print(f'O MENOR VALOR FOI: {min(rol)}')