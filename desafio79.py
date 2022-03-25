valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Adicionado com sucesso...')
    else:
        print('O valor ja existi!')
    res = str(input('Quer continuar? [S/N]'))
    if res in 'Nn':
         break
valores.sort()
print(f'Os valores da lista são{valores}')
