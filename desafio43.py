peso = float(input('Escreva seu peso:'))
altura = float(input('Escreva sua altura:'))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Você esta abaixo do peso seu IMC é {:.2f}'.format(imc))
elif imc > 18.5 and imc <= 25 :
    print('Você está no peso ideal seu IMC é {:.2f}'.format(imc))
elif imc > 25 and imc <= 30:
    print('Você está sobrepeso seu IMC é {:.2f}'.format(imc))
elif imc > 30 and imc <= 40:
    print('Você está obeso seu IMC é {:.2f}'.format(imc))
elif imc > 40:
    print('Você está em Obesidade Mórbida seu IMC é {:.2f}'.format(imc))

