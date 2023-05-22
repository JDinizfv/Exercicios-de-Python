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

