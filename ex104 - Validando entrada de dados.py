

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




print('-'*25)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')