from time import sleep

def maior(* núm): # fazendo o despacotamento, pois vai ser passado varios paramentos
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 3, 5, 6)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()