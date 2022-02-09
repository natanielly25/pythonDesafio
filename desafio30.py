n = int(input('Digite um número:'))
resultado = n % 2
if resultado == 0:
    print('Seu número é \033[34mPAR!')
else:
    print('Seu número é \033[31mÌMPAR!')
