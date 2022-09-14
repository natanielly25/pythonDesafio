def ficha(jog='<desconhecido>', gol=0):  # definição da função, se não informar o jogador ele é desconhecido se não informa aquantidade de gol será 0p
    print(f'O jogador {jog}  fez {gol} gol(s) no campeonato.')

#Programa principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: ")) #
if g.isnumeric(): #isnumeric para verificar se ele pode ser um número ou não
    g = int(g)
else:
    g = 0
if n.strip() == '': # strip elimina todos os espaço e se for igual a vazio chama a ficha de um jeito se não chama de outo
    ficha(gol=g)
else:
    ficha(n, g)
