listanum = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','catorze','quinze','dezesséis','dezesete','dezoito','dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num not in range(0,21):
    if num <= 0 or num >= 20:
        print('Número inválido!!')
        num = int(input('Digite um número entre 0 e 20: '))

print(f'Você digitou o número {listanum[num]}.')


while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ',end='')
print(f'Você digitou o número {listanum[numero]}.')



