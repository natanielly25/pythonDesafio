from time import sleep
distância = float(input('Qual a distância em km do seu objetivo?'))
if distância <= 200:
    print('Calculando a passagem... ')
    sleep(2)
    preço = distância  * 0.50
    print('Sua passagem custará R${:.2f}'.format(preço))
else:
    preço = distância * 0.45
print('Sua passagem custará R${:.2f}'.format(preço))
