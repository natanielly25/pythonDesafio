from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano \033[34m{}\033[m é Bissexto!'.format(ano))
else:
    print('Esse ano \033[34m{}\033[m não é Bissexto'.format(ano))