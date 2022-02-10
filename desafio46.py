from time import sleep
import emoji
print('{:*^60}'.format(' CONTAGEM REGRESSIVA! '))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[33m :fireworks: :boom: :fireworks: :boom: :fireworks: :boom: :fireworks: :boom: :fireworks: :boom:\033[m ', use_aliases=True))
