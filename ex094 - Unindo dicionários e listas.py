dados = list()
pessoa = dict()
soma = 0
mulheres = list()

while True:
    pessoa.clear()
    pessoa['Nome']=str(input('Nome: ')).capitalize().strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['Sexo'] == 'F':
            mulheres.append(pessoa['Nome'])
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade']=int(input('Idade: '))
    soma += pessoa['Idade']
    dados.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        print('Resposta inválida!')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(dados)} pessoas')
print(f'- A média de idade é de {(soma/len(dados)):.2f}')
print(f'- As mulheres cadastradas foram: ',end='')
for p in dados:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}',end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')

for p in dados:
    if p['Idade'] >=(soma/len(dados)):
        print(' ')
        for k,v in p.items():
            print(f'{k} = {v}',end='; ')
            print()
print('<< Encerrado >>')
