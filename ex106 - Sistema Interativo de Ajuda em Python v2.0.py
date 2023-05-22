c = ('\033[m', #0 - sem cores
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;47m',      #2 - Branco
    '\033[0;30;44m',       #3 - Azul
     '\033[0;30;42m')


def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)
    print(c[0],end='')


comando = ''
while True:
    titulo('Sistema de AJUDA PyHELP',4)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!',1)

