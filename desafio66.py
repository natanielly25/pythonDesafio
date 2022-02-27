n = soma = quant = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
       break
    soma += n
    quant += 1
print(f'Você digitou {quant} números a soma entre eles é {soma}.')