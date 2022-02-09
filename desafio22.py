nome = str(input('Digite seu nome completo:')).strip()#elimina os espaços no inicio e no final
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome te ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} lestras'.format(separa[0],len(separa[0])))