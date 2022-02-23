from random import randint
from time import sleep
computador = randint(0,5)
print('=-='* 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('=-='* 20)
acertou = False
palpites = 0
while not acertou:
      jogador = int(input('Em que número eu pensei?'))
      print('PROCESSANDO...')
      sleep(1)
      palpites += 1
      if jogador == computador:
          acertou = True
      else:
          if jogador < computador:
              print('\033[34mMais... Tente mais uma vez.\033[m')
          elif jogador > computador:
              print('\033[33mMenos... Tente mais uma vez.\033[m')
print('\033[32mACERTOU\033[m com \033[31m{}\033[m tentativas.'.format(palpites))