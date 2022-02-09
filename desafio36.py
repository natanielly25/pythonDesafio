valor = float(input('Qualo valor da casa?'))
salário = float(input('salário R$:'))
anos = int(input('Em quantos anos deseja pagar?'))
prestação = valor / (anos * 12)
mínimo = salário * 30 / 100
if prestação <= mínimo:
    print('\033[32mEMPRÉSTIMO APROVADO!!\033[m')
else:
    print('\033[31mEMPRÉSTIMO NEGADO\033[m, sua mensalidade ultrapassa o limite permitido.')

