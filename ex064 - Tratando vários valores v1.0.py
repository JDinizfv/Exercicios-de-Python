num = 0
totnum= 0
total = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        total += num
        totnum += 1
    else:
        pass
print('Parou!')
print('Você digitou {} números, e a soma entre eles é {}'.format(totnum,total))