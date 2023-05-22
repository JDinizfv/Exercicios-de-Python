primeiro = int(input('Qual o valor inicial?: '))
razão = int(input('Qual o valor da razão?: '))

termo = primeiro
cont = 0
meta = 10

while cont <= meta:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
    if cont == meta:
        print('Pausa!')
        meta = int(input('Quantos termos quer mostrar mais? '))
        if meta>0:
            meta += cont
        else:
            pass


print('Progressão realizada com {} termos mostrados)'.format(meta))
print('Fim!')

## ou

'''total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar mais? '))
print('Progressão realizada com {} termos mostrados'.format(total))
print('Fim!')
'''