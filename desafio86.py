matriz = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
for l in range(0, 3): # for de alimentação aonde vai colocar os valores na matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c} ]'))
for l in range(0, 3): # eles são for para mostrar a estrutura na tela
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='') # caso digite valores aleatoris eles vão ficar centralizado :^5
    print()