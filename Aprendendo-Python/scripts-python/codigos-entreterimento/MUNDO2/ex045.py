from random import choice
comp = ['PEDRA', 'PAPEL', 'TESOURA']
jog = str(input('COLOQUE PEDRA, PAPEL OU TESOURA: ')).upper().strip()
esco = choice(comp)
if esco == jog:
    print('NINGUÉM VENCEU')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
elif esco == 'PEDRA' and jog == 'PAPEL':
    print('VOCÊ GANHOU, PARABÉNS')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
elif esco == 'PAPEL' and jog == 'TESOURA':
    print('VOCÊ GANHOU, PARABÉNS')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
elif esco == 'TESOURA' and jog == 'PEDRA':
    print('VOCÊ GANHOU, PARABÉNS')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
elif jog == 'TESOURA' and esco == 'PEDRA':
    print('VOCÊ PERDEU E EU GANHEI')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
elif jog == 'PAPEL' and esco == 'TESOURA':
    print('VOCÊ PERDEU E EU GANHEI')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
elif jog == 'PEDRA' and esco == 'PAPEL':
    print('VOCÊ PERDEU E EU GANHEI')
    print('EU FIZ {} E VOCÊ FEZ {}'.format(esco, jog))
