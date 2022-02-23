from time import sleep
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
opção = 0
while opção != 5:
      print('''
      [ 1 ] SOMA
      [ 2 ] MULTIPLICAR
      [ 3 ] MAIOR
      [ 4 ] NOVOS NÚMEORS
      [ 5 ] SAIR DO PROGRAMA''')
      opção = int(input('Escolha uma opção:'))
      if opção == 1 :
            soma = n1 + n2
            print('A soma \033[32m{}\033[m mais \033[32m{}\033[m é \033[32m{}.\033[m'.format(n1, n2, soma))
      elif opção == 2 :
            produto = n1 * n2
            print('O resultado de \033[32m{}\033[m x \033[32m{}\033[m é \033[32m{}.\033[m'.format(n1, n2, produto))
      elif opção == 3 :
            if n1 > n2:
                  maior = n1
            else:
                  maior = n2
            print('O maior número entre \033[32m{}\033[m e \033[32m{}\033[m é \033[32m{}.\033[m.'.format(n1, n2, maior))
      elif opção == 4 :
            print('Informe os números novamente:')
            n1 = int(input('Digite o primeiro valor:'))
            n2 = int(input('Digite o segundo valor: '))
      elif opção == 5 :
            print('FINALIZANDO...')
            sleep(1)
      else:
            print('Opção INVALIDA!')
print('\033[33mFim do programa.\033[m')