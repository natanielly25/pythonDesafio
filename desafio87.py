matriz = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
spar = mai = scol = 0
for l in range(0, 3): # for de alimentação aonde vai colocar os valores na matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c} ]'))
for l in range(0, 3): # eles são for para mostrar a estrutura na tela
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='') # caso digite valores aleatoris eles vão ficar centralizado :^5
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos pares são {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]# soma da coluna e deixa ela fix oque vai variar é o valor da linha
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
         mai = matriz[1][c] # a linha ficara fixa e o que variar é os valores da coluna
    elif matriz[1][c] > mai:
         mai = matriz[1][c]
print(f'O maior valor da segunda coluna é {mai}.')
