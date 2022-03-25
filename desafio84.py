dado = list()
princ = list()
maior = menor = 0
while True:
    dado.append (str(input('Nome:')))
    dado.append(float(input('Seu peso:')))
    if len(princ) == 0:
        maior = menor = dado[1]
    else:
        if dado [1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    princ.append(dado[:])
    dado.clear()
    res = str(input('Quer continuar? [S/N]'))
    if res in 'Nn':
        break
print(f'Ao todo foram cadastrados {len(princ)} pessoas.')
print(f'O maior peso cadastrado é {maior}kg.')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f"O menor peso cadastrado é {menor}kg.")
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
