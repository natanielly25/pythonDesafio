from random import randint
v = 0
while True:
    jogador = int(input('Digite o seu número:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}. ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[32mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[32mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!\033[m')
            break
        print('Vamos jogar novamente...')
print(f'\033[33mGamer Over\033[m...Você venceu {v}')