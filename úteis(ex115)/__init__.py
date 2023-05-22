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


def escreva(text):
    print(42*'-')
    print(f'{text}'.center(42))
    print(42*'-')

def menu(lista):
    escreva('MENU PRINCIPAL')
    for i,v in enumerate(lista):
        print(f'\033[33m{i+1}-\033[33m \033[34m{v}\033[m')
    print(42 * '-')
    resposta = leiaint('\033[32mSua opção: \033[m')
    return resposta

def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        escreva('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1]= dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()