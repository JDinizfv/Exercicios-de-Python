def aumentar(valor=1,quantidade=0):
    """
    -> Função para realizar um aumento em porcentagem de um valor determinado.
    :param valor: Valor da variável.
    :param quantidade: Quantidade do aumento.
    :return: Valor atualizado.
    """
    valor = valor*(1+(quantidade/100))
    return valor

def diminuir(valor=1,quantidade=0):
    """
    -> Função para realizar um decréscimo em porcentagem de um valor determinado.
    :param valor: Valor da variável.
    :param quantidade: Quantidade do aumento.
    :return: Valor atualizado.
    """
    valor = valor*(1-(quantidade/100))
    return valor

def dobro(valor):
    """
    -> Função para dobrar um valor.
    :param valor: Valor
    :return: Valor dobrado
    """
    valor=valor*2
    return valor

def metade(valor):
    """
    -> Função para dividir pela metade um valor.
    :param valor: Valor.
    :return: Valor pela metade.
    """
    valor=valor/2
    return valor


