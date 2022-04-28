def voto(ano):
    from datetime import date # importado dentro da função pois so serve para essa funçãob e economiza memoria
    atual = date.today().year  # pegando o ano atual
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBTIGATORIO'


nasc = int(input("Em que ano você nasceu?"))
print(voto(nasc)) # pega os 2000 e joga dentro da importação ano