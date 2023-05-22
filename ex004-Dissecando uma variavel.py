text = input('Digite aqui seu texto: ')
print('O tipo primitivo desse texto é: ',type(text))

print('Só tem espaços?', text.isspace())
print('É um número?', text.isnumeric())
print('É alfabético?',text.isalpha())
print('É alfanumérico?',text.isalnum())
print('Está em maiúsculas?',text.isupper())
print('Está em minúsculas?',text.islower())
print('Está capitalizada?', text.istitle())



for letra in text:
    print('Para',letra,'temos: ')
    print('')
    print(text.isalpha(),'para alfabeto')
    print(text.isnumeric(),'para numérico')
    print(text.isalnum(),'para alfanumérico')
    print(text.isupper(),'para maiúscula')
    print(text.islower(),'para minúscula')
    print(text.isspace(),'para espaço')
    print('-------------------------------------------')