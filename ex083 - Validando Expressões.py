pilha = list()
exp = input('Digite a expressão: ')
print(exp)

for i in exp:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
