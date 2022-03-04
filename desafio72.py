cont = ('zero', 'um' , 'dois' , 'três', 'quatro', 'cinco', 'seis'
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quarto',
        'quinze', 'dezessis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20 para vê lo por extenso:'))
    if 0 <= n <= 20:
        break
print(f'Você digitou {cont[n]}.')
