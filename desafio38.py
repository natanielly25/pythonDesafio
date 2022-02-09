n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite um segundo númeor inteiro:'))
if n1 > n2:
    print('O \033[32mPRIMEIRO\033[m valor é maior. ')
elif n2 > n1:
    print('O \033[34mSEGUNDO\033[m valor é maior.')
else:
    n1 == n2
    print('\033[31mNÃO\033[m existe valor maior, os dois são iguais.')
