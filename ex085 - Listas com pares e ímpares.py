
lista = list()
pares = list()
impares = list()

for i in range(0,7):
    num = int(input(f'Digite o {i+1}º número: '))
    if num % 2 ==0:
        pares.append(num)
    elif num%2 == 1:
        impares.append(num)
lista.append(pares)
lista.append(impares)
lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]} ')
print(f'Os valores ímpares digitados foram: {lista[1]} ')


# Versão Professor

núm = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor %2 ==0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {núm[0]} ')
print(f'Os valores ímpares digitados foram: {núm[1]} ')