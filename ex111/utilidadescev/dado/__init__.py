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

def leiaint(n):
    """
    -> Função desenhada para guardar valores 'int' na memória.
    :param n: valor
    :return: valor de tipo 'int'

    Função criada por Jean Diniz baseado no exercício 104 do Curso em Video(Python).
    """
    while n.isnumeric() != True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n
