from random import randint
números =  randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Números aleatorias {números}')
for n in números:
    print(f'{n}', end='')
print(f'O maior número sorteado foi {max(números)}')
print(f'O menor número sorteado foi {min(números)}')
