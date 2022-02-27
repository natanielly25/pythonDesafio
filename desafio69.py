quant = homem = mulher20 = 0
while True:
    idade = int(input('Idade:'))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        quant += 1
    if sexo == 'M':
        homem +=1
    if sexo == 'F' and idade < 20:
        mulher20 +=1
    cad =' '
    while cad not in 'SN':
        cad = str(input('Deseja realizar mais algum cadastro? [S/N]')).strip().upper()[0]
    if cad == 'N':
        break
print(f'Total de homens cadastrados: \033[34m{homem}\033[m.')
print(f'Total de pessoas maiores de 18 anos: \033[34m{quant}\033[m.')
print(f'Total de mulheres com menos de 20 anos: \033[34m{mulher20}\033[m.')
print('Cadastro Finalizado!')



