while True:
     n = int(input('Digite o número que você que vê a tabuada:'))
     print('=' * 20)
     if n < 0:
         break
     for c in range(1, 11):
            print(f'{n} X {c} = {n*c}')
     print('=' * 20)
print('Tabuada Encerrada!')