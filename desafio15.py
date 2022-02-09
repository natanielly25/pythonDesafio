km = float(input('Quantos km rodado?'))
d = int(input('Qual a quantidade de dias?'))

preçof = (km * 0.15) + (d * 60)

print('O preço a pagar pelo o aluguel é R${:.2f}.'.format(preçof))
