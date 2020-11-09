# CÓDIGO FEITO PELO PROFESSOR

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas conseguem formar um TRIÂNGULO ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Com essas retas não é possivel formar um TRIÂNGULO!')
