
def fatorial(num=1, show=False):
    """"
    -> Função para determinar o valor de um número fatorial.
    :param num: Número Fatorial.
    :param show: Mostra cálculo por trás do resultado.
    :return: Cálculo fatorial do valor num.
    Função criada por Jean Diniz baseado no exercício 102 do Curso em Video(Python).
    """

    print('-'*20)
    sum = 1
    if show == True:
        print(f'Fatorial de {num}: ')
        for i in range(num,0,-1):
            if i == 1:
                print(f' {i} = ',end='')
            else:
                print(f' {i} x',end='')
                sum *= i
        return print(f'{sum}')
    elif show == False:
        for i in range(num, 0, -1):
            sum*=i
        return print(f'{sum}')

fatorial(int(input('Digite o número: ')),True)
help(fatorial)
