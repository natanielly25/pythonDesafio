total = quant = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto:'))
    valor = float(input('Valor do produto R$:'))
    cont +=1
    total += valor
    if valor >= 1000:
        quant += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    cad =' '
    while cad not in 'SN':
        cad = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if cad == 'N':
            break
print('Fim de consulta')
print(f'O total da compra foi R${total}')
print(f'Temos {quant} prodrutos custando mais de R$1000.00')
print(f'O produto mais barato é {barato} que custa R$ {menor:.2f}')
