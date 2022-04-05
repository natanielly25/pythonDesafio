def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno mede {larg} X {comp} que é {a}m²')


print(' Controle de Terreno ')
print('-'* 20)
l = float(input('A largura do Terreno (m):'))
c = float(input('O comprimento do Terreno(m):'))
área (l, c)
