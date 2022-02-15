#tabuada
num = int(input('Digote um número para vê sua tabuada:'))
for n in range(1, 11):
    print('{}  X  {:2}'.format(num, n, num*n))