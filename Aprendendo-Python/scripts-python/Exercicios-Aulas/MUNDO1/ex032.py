ano = int(input('Digite um ano: '))
div4 = ano % 4
div100 = ano % 100
div400 = ano % 400
if div4 == 0 and div100 != 0 or div400 == 0:
    print('O ANO É BISSEXTO!')
else:
    print('O ANO NÃO É BISSEXTO!')
