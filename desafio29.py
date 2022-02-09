velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('\33[31mMULTADO, Você ultrapaasou o limite de velocidade de 80km/h. ')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
else:
    print('\033[32mVelocidade permitida!')