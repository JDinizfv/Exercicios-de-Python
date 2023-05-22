


def notas(*num,sit=False):
    """
    -> Cria um dicionário com os dados e situação do Aluno
    :param num: Uma ou mais notas de Alunos (Aceitam várias)
    :param sit: Situação do Aluno (Valor opcional)
    :return: Dicionário com informações do Aluno

    Função criada por Jean Diniz baseado no exercício 105 do Curso em Video(Python).
    """
    data = dict()
    print('-'*25)
    media = sum(num)/len(num)
    data['Total']= len(num)
    data['Maior']= max(num)
    data['Menor']= min(num)
    data['Média']= media

    if sit == True:
        if media < 4:
            data['Situação'] = 'Péssima'
        elif 4 <= media < 7:
            data['Situação'] = 'Preocupante'
        elif 7 <= media <9:
            data['Situação'] = 'Boa'
        elif media>=9:
            data['Situação'] = 'Excelente'
    return data


resp = notas(0,1,10,0,5.7,sit=True)
print(resp)
help(notas)