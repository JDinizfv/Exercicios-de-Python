def escreva(text):
    print((len(text)+4)*'~')
    print(f'  {text}')
    print((len(text)+4)*'~')


texto = str(input('Digite o texto desejado: '))
escreva(texto)