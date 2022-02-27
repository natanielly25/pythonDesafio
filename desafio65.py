resp = 'S'
soma = quant = média = menor = maior = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] '))
média = soma/quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, média))

