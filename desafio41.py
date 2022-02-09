from datetime import date
atual = date.today().year
ano = int(input('Infome o seu ano de nascimento:'))
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos sua categoria é MIRIM.'.format(idade))
elif  idade > 9 and  idade <=14:
    print('Você tem {} anos sua categoria é INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos sua categoria é JÚNIOR.'.format(idade))
elif idade > 19 and idade <=25:
    print('Você tem {} anos sua categoria é SÊNIOR.'.format(idade))
elif idade > 25:
    print ('Você tem {} anos sua categoria é MASTER.'.format(idade))
