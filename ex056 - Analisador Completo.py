somaidade = 0
mediaidade = 0
maisvelho = 0
num020mulheres = 0
nomevelho = ''
print('-=' * 20)
for i in range(1,5):

    nome = input('Nº{}, qual seu nome?: '.format(i))
    idade = int(input(('Qual sua idade?: '.format(i))))
    print('Qual seu sexo? | [ 0 ] Feminino | [ 1 ] Masculino |'.format(i))
    sexo = int(input('Digite aqui: '))
    print('-=' * 20)

    #1
    somaidade += idade
    mediaidade = somaidade / 4

    #2
    if i == 1:
        maisvelho = idade
        nomevelho = nome
    else:
        if idade>maisvelho and sexo == 1:
            maisvelho = idade
            nomevelho = nome

    #3
    if sexo == 0 and idade<20:
        num020mulheres += 1





print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('Existem {} garotas abaixo de 20 anos '.format(num020mulheres))
print('O nome do homem mais velho é {}, e ele tem {} anos'.format(nomevelho,maisvelho))