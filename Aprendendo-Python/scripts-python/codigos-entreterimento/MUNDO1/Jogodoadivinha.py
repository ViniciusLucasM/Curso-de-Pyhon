# O JOGO FOI FEITO NO VSCODE, CASO VOCÊ FOR UTILIZAR ELE NO PYCHARM, RETIRE ESSE ENDEREÇO codigos-entreterimento/jogo-do-adivinha/ NOS MIXER.MUSIC.LOAD

from random import randint
from time import sleep
from pygame import mixer

opcao = 0
vitoria = 0
derrota = 0

while opcao != 9:
    print()
    print('[  1  ] \033[4;32mCOMEÇAR A JOGAR\033[m')
    print('[  2  ] \033[4;34mVER QUANTOS ACERTO E DERROTAS\033[m')
    print('[  9  ] \033[4;31mSAIR DO JOGO\033[m')
    opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
    if opcao == 1:
        comp = randint(0, 10)
        mixer.init()
        mixer.music.load('codigos-entreterimento/jogo-do-adivinha/somgame.mp3')
        mixer.music.play()
        print()
        print('\033[1;34m-=-' * 10)
        print('\033[4;33mBEM VINDO AO JOGO DO ADIVINHA\033[m')
        print('\033[1;34m-=--=--=--=--=--=--=--=--=--=-\033[m')
        print()
        print('\033[4;35mCARREGANDO...\033[m')
        sleep(2)
        print()
        print(
            '\033[1;32m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\033[m')
        print('  VOU PENSAR EM UM NÚMERO DE 0 ATÉ 10. TENTE ADIVINHAR...')
        print(
            '\033[1;32m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\033[m')
        print()
        print('ESTOU PENSANDO...')
        sleep(3)
        print('\033[4;33mPRONTO, PENSEI. AGORA TENTE ADIVINHAR\033[m')
        print()
        numad = int(input('COLOQUE O NÚMERO QUE VOCÊ ACHA QUE EU PENSEI: '))
        if numad == comp:
            print()
            mixer.music.stop()
            mixer.init()
            mixer.music.load(
                'codigos-entreterimento/jogo-do-adivinha/level-win.mp3')
            mixer.music.play()
            print(
                '\033[4;32mPARABÉNS, VOCÊ CONSEGUIU ADIVINHAR O NÚMERO QUE EU PENSEI...\033[m')
            vitoria += 1
            sleep(3)
            mixer.music.stop()
        else:
            print()
            mixer.music.stop()
            mixer.init()
            mixer.music.load(
                'codigos-entreterimento/jogo-do-adivinha/player-died.mp3')
            mixer.music.play()
            print(
                '\033[4;31mQUE PENA, VOCÊ NÃO CONSEGUIU ADIVINHAR O NÚMERO QUE EU TINHA PENSADO...\033[m')
            print('\033[4;33mO NÚMERO ERA {}\033[m'.format(comp))
            derrota += 1
            sleep(3)
            mixer.music.stop()
    elif opcao == 2:
        print()
        print('O JOGADOR TEVE UM TOTAL DE \033[1;32m{}\033[m VITÓRIAS E \033[1;31m{}\033[m DERROTAS'.format(
            vitoria, derrota))
    else:
        print()
        print('\033[4;31mOPÇÃO INDISPONIVEL!!!\033[4;31m')
