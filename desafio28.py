from random import randint
from time import sleep #faz o computador esperar algum tempo
computador = randint(0,5)# Faz um computador "pensar"
print('-*-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-*-' * 20)
jogador = int(input('Em que número eu pensei?'))#jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você VENCEU!!!!!')
else:
    print('GANHEI eu pensei no numero {} e não no {}.'.format(computador, jogador))