soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print('você infomrmou \033[32m{}\033[m números pares e a soma deles é \033[33m{}.\033[m'.format(cont, soma))