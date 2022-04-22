from time import sleep

def contador(i, f, p): # função def de contador Inicio(i), Fim(f) e Passos(p)
    if p < 0:
        p *= -1 # se o passo for negativo aqui está trocando para ele ser positivo
    if p == 0:
        p = 1 # caso o passo seja 0 ele recebe 1
    print('=-='* 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)

    if i < f: # se o inicio for maior que o final entra no while
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!!')
    else: # se não (o inicio for menor) entra no while
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!!')


contador(0, 100, 10)
contador(10, 0, 2)
print('=-='* 20)
print('Agora é sua vez de personalizar a contagem.')
ini = int(input('Ìnicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

