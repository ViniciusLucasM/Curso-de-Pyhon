import math
angulo = int(input('Digite um angulo: '))
sen = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)

print('O angulo {} tem como seno {:.2f}, coseno {:.2f} e tangente {:.2f}'.format(angulo, sen, cos, tang))
