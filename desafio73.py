time = ('FLAMENGO', 'CORINTHIAS' , 'PALMEIRAS' , 'ATLETICO-MG', 'CHAPECOENSE', 'BRAGANTINO', 'SAO PAULO',
        'AMERICA', 'INTERNACIONAL', 'SANTOS', 'CEARA', 'FORTALEZA', 'JUVENTUDE',
        'SPORT', 'BAHIA', 'VITORIA', 'FLUMINENCE', 'VASCO', 'GOIAS', 'CSA',)
print(time)
print('=-=' * 12)
print(f'Os 5 primeiros time são {time[0:5]}')
print('=-=' * 12)
print(f'Os ultimos  4 colocados são{time[-4:]}')
print('=-=' * 12)
print(f'OS times em ordem alfabetica{sorted(time)}')
print('=-=' * 12)
print(f'O time da CHAPECOENSE  se encontra na posição {time.index("CHAPECOENSE") +1}.')
