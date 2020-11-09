import math
angulo = int(input('Digite um angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O angulo {} tem como SENO {:.2f}, COSENO {:.2f} e TANGENTE {:.2f}'
      .format(angulo, sen, cos, tang))
