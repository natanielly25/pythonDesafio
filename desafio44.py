print('{:*^60}'.format(' \033[32mNutri-se Bem, opção de  Pagamento\033[m '))
produto = float(input('Preço do produto R$:'))
print('[ 1 ] á vista dinheiro/cheque .')
print('[ 2 ] á vista no cartão')
print('[ 3 ] em até 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
op = int(input(' Escolha uma das opção de pagamento: '))
if op == 1:
    valor = produto - (produto * 10 / 100)
elif op == 2:
    valor = produto - (produto * 5 /100)
elif op == 3:
    valor = produto
    parcela = valor / 2
    print('Seu compra séra parcelada em 2x R${:.2f} . '.format(parcela))
elif op == 4:
    valor = produto +(produto * 20 / 100)
    totalparcela = int(input('Quantas parcelas?'))
    parcela = valor / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparcela, parcela))
else:
    valor = 0
    print('\033[31mOpção invalida tente novamente.\033[m')
print('Sua compra vai custar R${:.2f}.'.format(valor))

