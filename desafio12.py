preço = float(input('Digite o preço do produto: R$'))
desc = preço - (preço * 5 /100)
print('O produto custa R${:.2f} com desconto de 5% vai custar R${:.2f}'.format(preço, desc))
