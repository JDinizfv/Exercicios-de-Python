

def leiaint(msg):
    """
    -> Função desenhada para guardar valores 'int' na memória.
    :param n: valor
    :return: valor de tipo 'int'

    Função criada por Jean Diniz baseado no exercício 104 do Curso em Video(Python).
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def leiafloat(msg):

    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não escolher um número')
            return 0
        else:
            return n




print('-'*25)
ni = leiaint('Digite um número inteiro: ')
nr = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {ni} e um número real {nr}')
