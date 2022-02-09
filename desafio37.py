n = int(input('Digite um número:'))
n1 = int(input('Escolha 1 para Binário: 2 para Octal: 3 Para Hexadecimal:'))
if n1 == 1:
     print('O número {} em binario é {}'.format(n, bin(n)[2:]))
elif n1 == 2:
    print('O númeor {} em Octal é {}'.format(n, oct(n)[2:]))
elif n1 == 3:
    print('O número {} em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida, tente novamente.')