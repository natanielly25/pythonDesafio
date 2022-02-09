from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de sua nascimento:'))
idade = atual - ano
if idade == 18:
    print('Chegou a hora do seu Alistamento Militar.')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos falta {} para o seu Alistamento.'.format(saldo))
    alistamento = atual + saldo
    print('Seu alistamento será em {}'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    alistamento = atual - saldo
    print('Seu alistamento foi em {}.'.format(alistamento))
