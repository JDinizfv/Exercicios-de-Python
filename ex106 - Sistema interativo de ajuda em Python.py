c = ('\033[m', #0 - sem cores
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;47m',      #2 - Branco
    '\033[0;30;44m',       #3 - Azul
     '\033[0;30;42m' ) #4 Verde)

def textoespecial(text,cor=0):
    """
    -> Função desenvolvida para personalizar títulos
    :param text: Título que deseja que apareça no programa
    :param cor: Escolha a cor de fundo do titulo
    :return: Titulo personalizado
    """
    print(c[cor],end='')
    print((len(text) + 4) * '~')
    print(f'  {text}')
    print((len(text) + 4) * '~')
    print(c[0],end='')


def pyhelp():
    """
    -> Função que agiliza o acesso a busca de ajuda das funções do Python
    :return: biblioteca da função
    """
    from time import sleep
    while True:
        textoespecial('SISTEMA DE AJUDA PyHELP',4)
        func = str(input('Função ou Biblioteca > ')).strip().lower()
        if func == 'fim':
            textoespecial('ATÉ LOGO!',1)
            break
        textoespecial(f'Acessando o manual do comando "{func}"',3)
        sleep(2)
        print(c[2],end='')
        print(help(func))
        print(c[0],end='')




pyhelp()
