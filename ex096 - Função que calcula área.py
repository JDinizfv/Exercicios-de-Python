
def area(largura,comprimento):
    area =largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m²')


print('     CONTROLE DE TERRENOS    ')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO [m): '))
area(largura,comprimento)