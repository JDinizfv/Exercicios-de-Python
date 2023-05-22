def leiadinheiro(text):
    """
    -> Retorna um valor Float em dinheiro
    :param valor:
    :return:
    """
    válido = False
    while not válido:
        valor = str(input(text)).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO!: \"{valor}\" é um preço inválido.\033[m')
        else:
            válido = True
            return float(valor)