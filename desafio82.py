num = list()
pares = list()
impares = list()
while True:
    num.append (int(input('Digite um numero:')))
    res = str(input('Quer continuar? [S/N]'))
    if res in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista de números é {num}')
print(f'Os números pares da lista são {pares}')
print(f'Os némeros impares da lista são {impares}')