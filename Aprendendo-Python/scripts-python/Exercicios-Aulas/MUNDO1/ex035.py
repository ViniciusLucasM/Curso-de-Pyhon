reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('')
    print('COM ESSAS RETAS É POSSIVEL CRIAR UM TRIÂNGULO!')
else:
    print('')
    print('COM ESSAS RETAS NÃO É POSSIVEL CRIAR UM TRIÂNGULO!')
