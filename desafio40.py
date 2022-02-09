n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
média = (n1 + n2) / 2
if média >= 7:
    print('Você foi \033[32mAPROVADO\033[m sua media é {}.'.format(média))
elif média < 5:
    print('Você foi \033[31mREPROVADO\033[m sua media é {}.'.format(média))
elif 7 > média >= 5:
    print('Você está na \033[33mRECUPERÇÃO\033[m sua média é {}.'.format(média))