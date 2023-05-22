j=0
count = 0
for i in range(0,501):
    if i % 2 != 0 and i % 3 == 0:
        print(i)
        j += i
        count += 1
    else:
        pass

print('Total: {} de um número total de {}'.format(j,count))
