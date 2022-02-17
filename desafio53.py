frase = str(input('Digite uma frase: ')).strip().upper()# tirou os espaços e jogou ela para maiusculas
palavras =  frase.split() #dividiu a palavra
junto = ''.join(palavras) #juntou desconsiderando os espaços entre elas
inverso =''
for letra in range(len(junto) - 1, - 1, - 1): # o len e junto ele pega e tira um, vai áte a letra -1 e vai voltando uma letra
    inverso += junto[letra]
print('O inverso de \033[32m{}\033[m é \033[33m{}\033[m'.format(junto, inverso))
if inverso == junto:
    print(' \033[34mÉ UM PALÍNDROMO!\033[m')
else:
    print(' \033[31mNÃO É PALÍNDROMO!\033[M')