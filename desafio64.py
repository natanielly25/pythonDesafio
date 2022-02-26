n = cont = soma = 0
n = int(input('Digite o número \033[32m999\033[m para parar:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite o número \033[32m999\033[m para parar:'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))