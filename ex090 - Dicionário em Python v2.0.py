'''alunos = dict()
nome = str(input('Nome: '))
alunos['Nome']=nome
media = int(input(f'Média de {nome}: '))
alunos['Média']= media
print(f'Nome é igual a {nome}')
print(f'Média igual a {media}')
if media>=7:
    print('Situação é igual a Aprovado!')
else:
    print('Situação é igual a Reprovado!')'''

# Versão professor

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média']= float(input(f'Média de {aluno["nome"]}: '))
if aluno['média']>=7:
    aluno['situação']='Aprovado'
elif 5<=aluno['média']<7:
    aluno['situação']='Recuperação'
else:
    aluno['situação']='Reprovado'
print(aluno)

for k,v in aluno.items():
    print(f'{k} é igual a {v}')
