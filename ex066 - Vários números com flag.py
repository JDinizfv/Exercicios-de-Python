count = 0
sum = 0
num = 0

while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    else:
        count += 1
        sum += num

print(f'Você digitou {count} números. A soma dos valores foi {sum}!')

