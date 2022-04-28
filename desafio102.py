def fatorial(n, show=False):
    '''
    -> Calcula p Fatorial de um número.
    :param n: O número de um número.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número.
    '''
    f = 1
    for c in range(n, 0, -1): # começando do numero até o 0 diminuindo de 1 em 1
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

        f *= c # o fatorial vai receber o fatorial vezes o contador
    return f

print(fatorial(5, show=True))