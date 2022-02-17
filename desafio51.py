print('==' * 15)
print('Primeiro termo e a razão de uma PA')
print('==' * 15)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end='-> ')
print('ACABOU')