from úteis import *
from time import sleep
import úteis





arq = 'cursoemvideo.txt'
if not úteis.arquivoexiste(arq):
    úteis.criararquivo(arq)

while True:
    resposta = úteis.menu(['Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        úteis.lerarquivo(arq)
    elif resposta == 2:
        úteis.escreva('NOVO CADASTRO')
        print('Vamos cadastrar o novo cliente...')
        sleep(1)
        nome = str(input('Digite o nome: ')).strip().capitalize()
        idade = leiaint('Digite a idade: ')
        cadastrar(arq,nome,idade)

        print('Cliente Cadastrado com Sucesso!')
    elif resposta == 3:
        úteis.escreva('Saindo do sistema')
        print('Encerrando o programa...')
        sleep(1)
        print('Obrigado!')
        break
    else:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')








