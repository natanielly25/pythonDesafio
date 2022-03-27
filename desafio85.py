num = ([], []) #vou adicionar o número na posição 0 ou 1
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° numero:'))
    if valor % 2 == 0:
         num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()# EM ORDEM OSVALORES DA LISTA DA POSIÇÃO 0
num[1].sort()
print(f'OS numeros pares são {num[0]}')
print(f'Os númeors ímpares são {num[1]}')
