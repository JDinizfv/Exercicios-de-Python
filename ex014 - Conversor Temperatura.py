ctemp = float(input('Digite a temperatura em ºC: '))
ftemp = ctemp * (9/5) + 32
ktemp = ctemp + 273.15

print('Convertendo temos {:.2f}ºF em graus Farenheit e {:.2f}ºK em graus Kelvin'.format(ftemp,ktemp))
