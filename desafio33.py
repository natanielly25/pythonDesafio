a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
#verificando o menor número
#if a < b and a < c:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and C > b:
    maior = c
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))


