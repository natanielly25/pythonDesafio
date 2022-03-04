números = (int(input('Digite o primeiro número:')),
        int(input('Digite o primeiro número:')),
        int(input('Digite o primeiro número:')),
        int(input('Digite o primeiro número:')))
print(f'Os números são {números}.')
print('=-=' * 12)
print(f'O número 9 apareceu {números.count(9)}.')
print('=-=' * 12)
if 3 in números:
        print(f'O valor 3 foi digitado na posição {números.index(3)+1}')
else:
        print('O valor 3 não foi digitado em nenhuma posição.')
print('=-=' * 12)
for n in números:
        if n % 2 == 0:
                print(n, end=' ')

