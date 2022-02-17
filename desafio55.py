maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pess)))
    if pess == 1: # se for a primeirra pessoa esssa pessoa se´ra o maior e o menor tambem
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} KG'.format(maior))
print('O menor peso foi {} KG'.format(menor))
