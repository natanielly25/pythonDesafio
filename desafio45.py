from random import randint
import emoji
print('{:=^60}'.format(' \033[34mPedra, Papel, Tesoura\033[m '))
op = ('\033[33mPedra\033[m', '\033[36mPapel\033[m', '\033[31mTesoura\033[m')
computador = randint(0, 2)
print('''
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tersoura''')
jogador = int(input('Qual sua opção? '))
print('**' * 12)
print('Computador jogou, {} '.format(op[computador]))
print('Jogador jogou, {}'.format(op[jogador]))
print('**' * 12)
if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print(emoji.emojize('\033[35mEMPATE! :astonished_face:\033[m', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[32mJOGADOR VENCEU!:sunglasses:\033[m', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[32mCOMPUTADOR VENCEU!:sunglasses:\033[m', use_aliases=True))
    else:
        print('Jogada \033[31mINVALIDA!![m')
elif computador == 1: #computador jogou Papel
    if jogador == 0:
        print(emoji.emojize('\033[32mCOMPUTADOR VENCEU!:sunglasses:\033[m', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[35mEMPATE! :astonished_face:\033[m', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[32mJOGADOR VENCEU!:sunglasses:\033[m', use_aliases=True))
    else:
        print('Jogada \033[31mINVÁLIDA!![m')
elif computador == 2: #computador jogou Tersoura
    if jogador == 0:
        print(emoji.emojize('\033[32mJOGADOR VENCEU!:sunglasses:\033[m', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[32mCOMPUTADOR VENCEU!:sunglasses:\033[m', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[35mEMPATE! :astonished_face:\033[m', use_aliases=True))
    else:
        print('Jogada \033[31mINVÁLIDA!![m')