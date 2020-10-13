#import random
#numAle = random.randint(0, 5)
#desco = int(input('Digite o número escolhido: '))
# if desco == numAle:
#    print('PARABÉNS, VOCÊ ADIVINHOU O NÚMERO')
# else:
#    print('VOCÊ NÃO CONSEGUIU ADIVINHAR O NÚMERO')
#print('O NÚMERO SORTEADO ERA {}'.format(numAle))

# CÓDIGO DO PROFESSOR
from random import randint
# Essa biblioteca serve para fazer o computador demorar um pouco para executar o proximo comando.
from time import sleep
computador = randint(0, 5)  # FAZ O COMPUTADOR SORTEAR UM NÚMERO DE 0 A 5.
print()
print('-=-'*20)
print('VOU PENSAR EM UM NÚMERO DE 0 À 5. TENTE ADIVINHAR...')
print('-=-'*20)
print()
jogador = int(input('DIGITE O NÚMERO NO QUAL VOCÊ ACHA QUE EU PENSEI: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\033[1;32mPARABÉNS, VOCÊ ADIVINHOU O NÚMERO!\033[m')
else:
    print('\033[1;33mPERDEU, VOCÊ NÃO CONSEGUIU ADIVINHAR O NÚMERO! O NÚMERO QUE EU TINHA PENSADO ERA {}\033[m'.format(computador))
