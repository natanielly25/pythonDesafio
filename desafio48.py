#soma impares multiplos de 3 intervalo de 1 até 500
soma = 0
cont = 0
for n in range(1, 501, 2):
      if n % 3 == 0:
          cont = cont +1
          soma = soma + n
print('A soma de todos {}  valores é {}'.format(cont, soma))
