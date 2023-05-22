from time import sleep

def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    sleep(1)
    for i in num:
        print(i,end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num)==0:
        print(f'O maior valor informado foi {len(num)}.')
    else:
        print(f'O maior valor informado foi {max(num)}.')


maior(5,2,6,3,1,8)
maior(5,2,8,9,10)
maior(20,3,1)
maior(50,7,40,2)
maior()