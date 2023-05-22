def aumentar(valor=1,quantidade=0,format=False,moeda='R$'):
    """
    -> Função para realizar um aumento em porcentagem de um valor determinado.
    :param valor: Valor da variável.
    :param quantidade: Quantidade do aumento.
    :param format: Quando True formata o valor em unidades monetárias.
    :param moeda: Moeda utilizada para conversão monetária
    :return: Valor atualizado.
    """
    valor = valor*(1+(quantidade/100))
    if format==True:
        valor = f'{moeda}{valor:.2f}'.replace('.',',')
    return valor


def diminuir(valor=1,quantidade=0,format=False,moeda='R$'):
    """
    -> Função para realizar um decréscimo em porcentagem de um valor determinado.
    :param valor: Valor da variável.
    :param quantidade: Quantidade do aumento.
    :param format: Quando True formata o valor em unidades monetárias.
    :param moeda: Moeda utilizada para conversão monetária
    :return: Valor atualizado.
    """
    valor = valor*(1-(quantidade/100))
    if format==True:
        valor = f'{moeda}{valor:.2f}'.replace('.',',')
    return valor

def dobro(valor=0,format=False,moeda='R$'):
    """
    -> Função para dobrar um valor.
    :param valor: Valor
    :param format: Quando True formata o valor em unidades monetárias.
    :param moeda: Moeda utilizada para conversão monetária
    :return: Valor dobrado
    """
    valor=valor*2
    if format==True:
        valor = f'{moeda}{valor:.2f}'.replace('.',',')
    return valor

def metade(valor=0,format=False,moeda='R$'):
    """
    -> Função para dividir pela metade um valor.
    :param valor: Valor.
    :param format: Quando True formata o valor em unidades monetárias.
    :param moeda: Moeda utilizada para conversão monetária
    :return: Valor pela metade.
    """
    valor=valor/2
    if format==True:
        valor = f'{moeda}{valor:.2f}'.replace('.',',')
    return valor

def moeda(preço=0,moeda='R$'):
    """
    -> Moeda para converter em valores monetários.
    :param preço: Valor a ser convertido
    :param moeda: Moeda de escolha para a conversão
    :return: Valor convertido
    """
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,aumenta=0,diminui=0,format=False,moeda='R$'):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda}{preço:.2f}'.replace('.',','))
    print(f'Dobro do preço:  \t{dobro(preço,True,moeda):>8}')
    print(f'Metade do preço: \t{metade(preço, True,moeda):>8}')
    print(f'{aumenta}% de aumento:  \t{aumentar(preço,aumenta,True,moeda)}')
    print(f'{diminui}% de redução:  \t{diminuir(preço,diminui,True,moeda)}')
    print('-' * 30)