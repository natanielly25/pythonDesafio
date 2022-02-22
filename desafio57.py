sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]#tirou os espaçoes, jogou para maiuscula e prgou a primeira letra
while sexo not in 'MmFf': #enquento o sexo não estiver em masculino e feminino
     sexo = str(input('Opção invalida digite novamente o seu sexo.')).strip().upper()[0]
print('Sexo {} registtado com sucesso.'.format(sexo))