salário = float(input('Digite seu sálario R$:'))
if salário > 1250:
    aumento = salário + (salário * 10 / 100)
if salário <= 1250:
    aumento = salário + (salário * 15 / 100)
print('Você teve um aumento de R${:.2f}'.format(aumento))