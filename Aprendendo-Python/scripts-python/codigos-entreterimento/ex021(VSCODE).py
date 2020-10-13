from pygame import mixer

mixer.init()
# Para trocar a musica, coloque o nome depois da /.
mixer.music.load('codigos-entreterimento/trapdochaves.mp3')
mixer.music.play()
print()
input('\033[4;33;44mCURTE ESSA OBRA DE ARTE MEU GUERREIRO!!!\033[m')
