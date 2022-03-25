valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {cont}:')))
maior=max(valores)
menor=min(valores)
print(f'Os valores da lista são {valores}')
print(f'O maior valor contido na lista é {max(valores)} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
     print(f'{i}... ',end='')
print(f' O menor valor contido na lista é {min(valores)} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')
print('Fim do programa Lista.')
