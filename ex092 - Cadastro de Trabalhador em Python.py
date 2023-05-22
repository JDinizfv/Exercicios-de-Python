from _datetime import datetime

'''dados = dict()

nome = str(input('Nome: '))
dados['Nome']=nome
anonasc = int(input('Ano de Nascimento: '))
hoje = datetime.now().year
idade = hoje - anonasc
dados['Idade']= idade
dados['Ano Nascimento']=anonasc
carteira = int(input('Carteira de Trabalho: '))
dados['CTPS']=carteira
if carteira != 0:
    anocontrato = int(input('Ano de Contratação: '))
    dados['Ano de Contratação']=anocontrato
    salario = int(input('Salário: '))
    dados['Salário'] =salario
    aposentado = idade + (35 - (hoje-anocontrato))
    dados['Ano Aposentadoria']=aposentado
else:
    pass
print('-=-'*50)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')'''

#Versão Professor

dados= dict()
dados['nome']=str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade']=datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho: '))

if dados['ctps'] != 0:
    dados['contratação']= int(input('Ano de Contratação: '))
    dados['salário']=int(input('Salário: '))
    dados['aposentadoria']= dados['idade'] + ((dados['contratação']+35) - datetime.now().year)
print('-=-'*50)
print(dados)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')