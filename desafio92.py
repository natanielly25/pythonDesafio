from datetime import datetime
dados = dict()
dados ['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: ' ))
dados ['idade'] = datetime.now().year - nasc # pegando o ano atual menos a dta de nascimento
dados['ctos'] = int(input('Carteira de trabalho (0 não tem):'))
if dados['ctos'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')