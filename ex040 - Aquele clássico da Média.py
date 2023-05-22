n1 = float(input('Qual a primeira nota?: '))
n2 = float(input('Qual a segunda nota?: '))

media = (n1 + n2)/2

if media < 5:
    print('Sua média foi de {:.1f}. Você está REPROVADO! Se dedique mais aos estudos da próxima vez'.format(media))
elif media>=5 and media<7:
    print('Sua média foi de {:.1f}. Você está de RECUPERAÇÃO! Aproveite o tempo livre para estudar. Boa Sorte!'.format(media))
elif media>= 7 and media<=10:
    print('Sua média foi de {:.1f}. Você está APROVADO! Parabéns e Boas Férias'.format(media))
else:
    print('Insira valores válidos!')