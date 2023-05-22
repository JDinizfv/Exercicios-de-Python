alunos = []
aluno = dict()
cont = 1


while True:
    nome = str(input(f'Nome do {cont}º aluno: '))
    nota = int(input(f'Nota de {nome}: '))
    aluno['Nome']= nome
    aluno['Nota']= nota
    alunos.append(aluno.copy())
    cont +=1
    resp = str(input('Deseja continuar?: [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta Inválida!')
        resp = str(input('Deseja continuar?: [S/N] ')).upper().strip()[0]
    if resp == 'N':
            break
print('Obrigado por usar o programa!')
print(alunos)