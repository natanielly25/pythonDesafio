jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partigadas {jogador ["nome"] } jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}?')))
    jogador ['gols'] = partidas[:]
    jogador ['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continuar [S/N}:')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if res == 'N':
        break
print('=-='* 20)
print('cod ', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('=-='* 20)
for k, v in enumerate(time):
    print(f' {k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('---=---'* 15)
while True:
    busca = int(input('Mostar dados de qual jogador?'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {bsuca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'   No {i+1}° jogo fez {g} gols.')
        print('==-=='* 15)
    print('<<Volte Sempre>>')


