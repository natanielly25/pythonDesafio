números = list()
for cont in range(0, 5):
    n = int(input('Digite um número:'))
    if cont == 0 :  # adiciona o primeiro valor na posição 1
        números.append(n)
        print('Adicionado ao final da lista...')
    elif n > números [-1]: # se o números for maior que o ultimo elemento
        números.append(n)
    else:
        pos = 0  # vai varrendo a lista e verificando se o número é maior ou menor da lista ai ele coloca entre esse números maior e menor
        while pos < len(números):
            if n <= números[pos]:
                números.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os números da lista em ordem são {números}')
