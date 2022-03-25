valores = list()
while True:
    valores.append(int(input('Digite um Número:')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os númeors da lista são {len(valores)} ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 NÃO faz parte da lista!')
